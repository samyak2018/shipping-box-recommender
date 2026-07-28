from django.contrib import admin

from .models import Order, OrderItem, Product, ShippingBox


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "length",
        "width",
        "height",
        "weight",
        "created_at",
    )
    search_fields = ("name",)


@admin.register(ShippingBox)
class ShippingBoxAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "internal_length",
        "internal_width",
        "internal_height",
        "max_weight",
        "cost",
        "is_active",
    )
    list_filter = ("is_active",)
    search_fields = ("name",)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ("product", "quantity")
    can_delete = False


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at",
    )
    inlines = (OrderItemInline,)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        "order",
        "product",
        "quantity",
    )
    search_fields = ("product__name",)