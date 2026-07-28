from orders.models import ShippingBox


def calculate_product_volume(product):
    return product.length * product.width * product.height


def calculate_box_volume(box):
    return (
        box.internal_length
        * box.internal_width
        * box.internal_height
    )


def calculate_order_weight(order):
    total_weight = 0

    for item in order.items.all():
        total_weight += item.product.weight * item.quantity

    return total_weight


def calculate_order_volume(order):
    total_volume = 0

    for item in order.items.all():
        product_volume = calculate_product_volume(item.product)
        total_volume += product_volume * item.quantity

    return total_volume


def product_fits_box(product, box):
    """
    Check whether a product can fit inside a box.

    Sorting dimensions allows the product to be rotated
    before comparing it with the box dimensions.
    """
    product_dimensions = sorted([
        product.length,
        product.width,
        product.height,
    ])

    box_dimensions = sorted([
        box.internal_length,
        box.internal_width,
        box.internal_height,
    ])

    return all(
        product_dimension <= box_dimension
        for product_dimension, box_dimension
        in zip(product_dimensions, box_dimensions)
    )


def all_products_fit_dimensions(order, box):
    for item in order.items.select_related("product"):
        if not product_fits_box(item.product, box):
            return False

    return True

def is_box_valid(order, box, total_weight=None, total_volume=None):
    if total_weight is None:
        total_weight = calculate_order_weight(order)

    if total_volume is None:
        total_volume = calculate_order_volume(order)

    if total_weight > box.max_weight:
        return False

    if total_volume > calculate_box_volume(box):
        return False

    if not all_products_fit_dimensions(order, box):
        return False

    return True


def get_valid_boxes(order):
    total_weight = calculate_order_weight(order)
    total_volume = calculate_order_volume(order)

    boxes = ShippingBox.objects.filter(is_active=True)

    valid_boxes = []

    for box in boxes:
        if is_box_valid(
            order,
            box,
            total_weight=total_weight,
            total_volume=total_volume,
        ):
            valid_boxes.append(box)

    return valid_boxes


def recommend_box(order):
    """
    Return the cheapest valid active box.

    Box volume is used as the tie-breaker when multiple
    valid boxes have the same cost.
    """
    valid_boxes = get_valid_boxes(order)

    if not valid_boxes:
        return None

    return min(
        valid_boxes,
        key=lambda box: (
            box.cost,
            calculate_box_volume(box),
        ),
    )