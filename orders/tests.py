from decimal import Decimal

from django.test import TestCase

from django.urls import reverse

from .forms import OrderCreateForm

from .models import Order, OrderItem, Product, ShippingBox
from .services.box_recommender import (
    calculate_box_volume,
    calculate_order_volume,
    calculate_order_weight,
    calculate_product_volume,
    get_valid_boxes,
    is_box_valid,
    product_fits_box,
    recommend_box,
)


class BoxRecommenderTests(TestCase):

    def setUp(self):
        self.mouse = Product.objects.create(
            name="Wireless Mouse",
            length=Decimal("12.00"),
            width=Decimal("7.00"),
            height=Decimal("4.00"),
            weight=Decimal("0.15"),
        )

        self.keyboard = Product.objects.create(
            name="Keyboard",
            length=Decimal("45.00"),
            width=Decimal("15.00"),
            height=Decimal("4.00"),
            weight=Decimal("0.80"),
        )

        self.small_box = ShippingBox.objects.create(
            name="Small Box",
            internal_length=Decimal("20.00"),
            internal_width=Decimal("15.00"),
            internal_height=Decimal("10.00"),
            max_weight=Decimal("2.00"),
            cost=Decimal("1.50"),
        )

        self.medium_box = ShippingBox.objects.create(
            name="Medium Box",
            internal_length=Decimal("50.00"),
            internal_width=Decimal("30.00"),
            internal_height=Decimal("20.00"),
            max_weight=Decimal("10.00"),
            cost=Decimal("2.50"),
        )

        self.large_box = ShippingBox.objects.create(
            name="Large Box",
            internal_length=Decimal("70.00"),
            internal_width=Decimal("50.00"),
            internal_height=Decimal("40.00"),
            max_weight=Decimal("25.00"),
            cost=Decimal("4.00"),
        )

        self.order = Order.objects.create()

        OrderItem.objects.create(
            order=self.order,
            product=self.mouse,
            quantity=2,
        )

        OrderItem.objects.create(
            order=self.order,
            product=self.keyboard,
            quantity=1,
        )

    def test_calculate_product_volume(self):
        volume = calculate_product_volume(self.mouse)

        self.assertEqual(volume, Decimal("336.00"))

    def test_calculate_box_volume(self):
        volume = calculate_box_volume(self.medium_box)

        self.assertEqual(volume, Decimal("30000.00"))

    def test_calculate_order_weight(self):
        weight = calculate_order_weight(self.order)

        self.assertEqual(weight, Decimal("1.10"))

    def test_calculate_order_volume(self):
        volume = calculate_order_volume(self.order)

        self.assertEqual(volume, Decimal("3372.00"))

    def test_product_fits_box(self):
        self.assertTrue(
            product_fits_box(
                self.keyboard,
                self.medium_box
            )
        )

    def test_product_fits_box_after_rotation(self):
        product = Product.objects.create(
            name="Rotatable Product",
            length=Decimal("20.00"),
            width=Decimal("10.00"),
            height=Decimal("5.00"),
            weight=Decimal("1.00"),
        )

        box = ShippingBox.objects.create(
            name="Rotation Box",
            internal_length=Decimal("10.00"),
            internal_width=Decimal("5.00"),
            internal_height=Decimal("20.00"),
            max_weight=Decimal("5.00"),
            cost=Decimal("2.00"),
        )

        self.assertTrue(
            product_fits_box(product, box)
        )

    def test_product_does_not_fit_when_too_large(self):
        oversized_product = Product.objects.create(
            name="Long Product",
            length=Decimal("100.00"),
            width=Decimal("5.00"),
            height=Decimal("5.00"),
            weight=Decimal("1.00"),
        )

        self.assertFalse(
            product_fits_box(
                oversized_product,
                self.medium_box
            )
        )

    def test_box_invalid_when_order_is_too_heavy(self):
        heavy_product = Product.objects.create(
            name="Heavy Product",
            length=Decimal("10.00"),
            width=Decimal("10.00"),
            height=Decimal("10.00"),
            weight=Decimal("5.00"),
        )

        order = Order.objects.create()

        OrderItem.objects.create(
            order=order,
            product=heavy_product,
            quantity=1,
        )

        self.assertFalse(
            is_box_valid(order, self.small_box)
        )

    def test_box_invalid_when_total_volume_is_too_large(self):
        cube = Product.objects.create(
            name="Cube",
            length=Decimal("10.00"),
            width=Decimal("10.00"),
            height=Decimal("10.00"),
            weight=Decimal("0.10"),
        )

        order = Order.objects.create()

        OrderItem.objects.create(
            order=order,
            product=cube,
            quantity=4,
        )

        self.assertFalse(
            is_box_valid(order, self.small_box)
        )

    def test_get_valid_boxes(self):
        valid_boxes = get_valid_boxes(self.order)

        self.assertNotIn(self.small_box, valid_boxes)
        self.assertIn(self.medium_box, valid_boxes)
        self.assertIn(self.large_box, valid_boxes)

    def test_inactive_box_is_ignored(self):
        inactive_box = ShippingBox.objects.create(
            name="Discontinued Box",
            internal_length=Decimal("50.00"),
            internal_width=Decimal("30.00"),
            internal_height=Decimal("20.00"),
            max_weight=Decimal("10.00"),
            cost=Decimal("0.50"),
            is_active=False,
        )

        valid_boxes = get_valid_boxes(self.order)

        self.assertNotIn(inactive_box, valid_boxes)

    def test_recommend_cheapest_valid_box(self):
        recommended_box = recommend_box(self.order)

        self.assertEqual(
            recommended_box,
            self.medium_box
        )

    def test_cheaper_valid_box_is_preferred_over_smaller_box(self):
        cheaper_large_box = ShippingBox.objects.create(
            name="Cheap Large Box",
            internal_length=Decimal("60.00"),
            internal_width=Decimal("40.00"),
            internal_height=Decimal("30.00"),
            max_weight=Decimal("20.00"),
            cost=Decimal("2.00"),
        )

        recommended_box = recommend_box(self.order)

        self.assertEqual(
            recommended_box,
            cheaper_large_box
        )

    def test_smaller_box_selected_when_cost_is_equal(self):
        ShippingBox.objects.create(
            name="Same Cost Large Box",
            internal_length=Decimal("60.00"),
            internal_width=Decimal("40.00"),
            internal_height=Decimal("30.00"),
            max_weight=Decimal("20.00"),
            cost=Decimal("2.50"),
        )

        recommended_box = recommend_box(self.order)

        self.assertEqual(
            recommended_box,
            self.medium_box
        )

    def test_recommend_box_returns_none_when_no_box_fits(self):
        huge_product = Product.objects.create(
            name="Huge Product",
            length=Decimal("200.00"),
            width=Decimal("200.00"),
            height=Decimal("200.00"),
            weight=Decimal("100.00"),
        )

        order = Order.objects.create()

        OrderItem.objects.create(
            order=order,
            product=huge_product,
            quantity=1,
        )

        recommended_box = recommend_box(order)

        self.assertIsNone(recommended_box)


class OrderFormAndViewTests(TestCase):
    def setUp(self):
        self.mouse = Product.objects.create(
            name="Wireless Mouse",
            length=Decimal("12.00"),
            width=Decimal("7.00"),
            height=Decimal("4.00"),
            weight=Decimal("0.15"),
        )

        self.keyboard = Product.objects.create(
            name="Keyboard",
            length=Decimal("45.00"),
            width=Decimal("15.00"),
            height=Decimal("4.00"),
            weight=Decimal("0.80"),
        )

        self.medium_box = ShippingBox.objects.create(
            name="Medium Box",
            internal_length=Decimal("50.00"),
            internal_width=Decimal("30.00"),
            internal_height=Decimal("20.00"),
            max_weight=Decimal("10.00"),
            cost=Decimal("2.50"),
        )

    def test_order_form_contains_product_fields(self):
        form = OrderCreateForm()

        self.assertIn(
            f"product_{self.mouse.id}",
            form.fields,
        )

        self.assertIn(
            f"product_{self.keyboard.id}",
            form.fields,
        )

    def test_order_form_rejects_empty_order(self):
        form = OrderCreateForm(
            data={
                f"product_{self.mouse.id}": 0,
                f"product_{self.keyboard.id}": 0,
            }
        )

        self.assertFalse(form.is_valid())

        self.assertIn(
            "Please select at least one product.",
            form.non_field_errors(),
        )

    def test_order_form_accepts_valid_quantities(self):
        form = OrderCreateForm(
            data={
                f"product_{self.mouse.id}": 2,
                f"product_{self.keyboard.id}": 1,
            }
        )

        self.assertTrue(form.is_valid())

    def test_order_form_rejects_negative_quantity(self):
        form = OrderCreateForm(
            data={
                f"product_{self.mouse.id}": -1,
                f"product_{self.keyboard.id}": 0,
            }
        )

        self.assertFalse(form.is_valid())

    def test_create_order_page_loads_successfully(self):
        response = self.client.get(
            reverse("orders:create_order")
        )

        self.assertEqual(
            response.status_code,
            200,
        )

    def test_create_order_page_uses_correct_template(self):
        response = self.client.get(
            reverse("orders:create_order")
        )

        self.assertTemplateUsed(
            response,
            "orders/order_create.html",
        )

    def test_empty_order_submission_does_not_create_order(self):
        response = self.client.post(
            reverse("orders:create_order"),
            data={
                f"product_{self.mouse.id}": 0,
                f"product_{self.keyboard.id}": 0,
            },
        )

        self.assertEqual(response.status_code, 200)

        self.assertEqual(
            Order.objects.count(),
            0,
        )

        self.assertContains(
            response,
            "Please select at least one product.",
        )

    def test_valid_submission_creates_order(self):
        self.client.post(
            reverse("orders:create_order"),
            data={
                f"product_{self.mouse.id}": 2,
                f"product_{self.keyboard.id}": 1,
            },
        )

        self.assertEqual(
            Order.objects.count(),
            1,
        )

    def test_valid_submission_creates_correct_order_items(self):
        self.client.post(
            reverse("orders:create_order"),
            data={
                f"product_{self.mouse.id}": 2,
                f"product_{self.keyboard.id}": 1,
            },
        )

        order = Order.objects.get()

        mouse_item = OrderItem.objects.get(
            order=order,
            product=self.mouse,
        )

        keyboard_item = OrderItem.objects.get(
            order=order,
            product=self.keyboard,
        )

        self.assertEqual(mouse_item.quantity, 2)
        self.assertEqual(keyboard_item.quantity, 1)

    def test_zero_quantity_product_does_not_create_order_item(self):
        self.client.post(
            reverse("orders:create_order"),
            data={
                f"product_{self.mouse.id}": 3,
                f"product_{self.keyboard.id}": 0,
            },
        )

        order = Order.objects.get()

        self.assertTrue(
            OrderItem.objects.filter(
                order=order,
                product=self.mouse,
            ).exists()
        )

        self.assertFalse(
            OrderItem.objects.filter(
                order=order,
                product=self.keyboard,
            ).exists()
        )

    def test_valid_submission_redirects_to_order_detail(self):
        response = self.client.post(
            reverse("orders:create_order"),
            data={
                f"product_{self.mouse.id}": 2,
                f"product_{self.keyboard.id}": 1,
            },
        )

        order = Order.objects.get()

        expected_url = reverse(
            "orders:order_detail",
            args=[order.id],
        )

        self.assertRedirects(
            response,
            expected_url,
        )

    def test_order_detail_page_loads_successfully(self):
        order = Order.objects.create()

        OrderItem.objects.create(
            order=order,
            product=self.mouse,
            quantity=2,
        )

        response = self.client.get(
            reverse(
                "orders:order_detail",
                args=[order.id],
            )
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        self.assertTemplateUsed(
            response,
            "orders/order_detail.html",
        )

    def test_order_detail_displays_order_items(self):
        order = Order.objects.create()

        OrderItem.objects.create(
            order=order,
            product=self.mouse,
            quantity=2,
        )

        response = self.client.get(
            reverse(
                "orders:order_detail",
                args=[order.id],
            )
        )

        self.assertContains(
            response,
            "Wireless Mouse",
        )

        self.assertContains(
            response,
            "2",
        )

    def test_order_detail_displays_recommended_box(self):
        order = Order.objects.create()

        OrderItem.objects.create(
            order=order,
            product=self.mouse,
            quantity=2,
        )

        response = self.client.get(
            reverse(
                "orders:order_detail",
                args=[order.id],
            )
        )

        self.assertContains(
            response,
            "Medium Box",
        )

        self.assertContains(
            response,
            "2.50",
        )

    def test_order_detail_displays_message_when_no_box_fits(self):
        huge_product = Product.objects.create(
            name="Huge Product",
            length=Decimal("500.00"),
            width=Decimal("500.00"),
            height=Decimal("500.00"),
            weight=Decimal("100.00"),
        )

        order = Order.objects.create()

        OrderItem.objects.create(
            order=order,
            product=huge_product,
            quantity=1,
        )

        response = self.client.get(
            reverse(
                "orders:order_detail",
                args=[order.id],
            )
        )

        self.assertContains(
            response,
            "No suitable shipping box is available for this order.",
        )

    def test_nonexistent_order_returns_404(self):
        response = self.client.get(
            reverse(
                "orders:order_detail",
                args=[99999],
            )
        )

        self.assertEqual(
            response.status_code,
            404,
        )