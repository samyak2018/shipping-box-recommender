from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render

from .forms import OrderCreateForm
from .models import Order, OrderItem, Product
from .services.box_recommender import (
    calculate_order_volume,
    calculate_order_weight,
    recommend_box,
)


def create_order(request):
    if request.method == "POST":
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            with transaction.atomic():
                order = Order.objects.create()

                for product in Product.objects.all():
                    quantity = form.cleaned_data.get(
                        f"product_{product.id}"
                    )

                    if quantity and quantity > 0:
                        OrderItem.objects.create(
                            order=order,
                            product=product,
                            quantity=quantity,
                        )

            return redirect(
                "orders:order_detail",
                order_id=order.id,
            )

    else:
        form = OrderCreateForm()

    return render(
        request,
        "orders/order_create.html",
        {"form": form},
    )


def order_detail(request, order_id):
    order = get_object_or_404(
        Order.objects.prefetch_related("items__product"),
        id=order_id,
    )

    recommended_box = recommend_box(order)
    total_weight = calculate_order_weight(order)
    total_volume = calculate_order_volume(order)

    context = {
        "order": order,
        "recommended_box": recommended_box,
        "total_weight": total_weight,
        "total_volume": total_volume,
    }

    return render(
        request,
        "orders/order_detail.html",
        context,
    )