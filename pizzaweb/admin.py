from django.contrib import admin
from .models import Pizza, Order, OrderItem


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "price",
        "is_available",
    )

    list_filter = (
        "is_available",
    )

    search_fields = (
        "name",
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "full_name",
        "phone",
        "total_price",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "created_at",
    )

    search_fields = (
        "full_name",
        "phone",
        "user__username",
    )


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "order",
        "pizza",
        "quantity",
        "price",
    )