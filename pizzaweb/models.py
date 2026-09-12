from django.db import models
from django.contrib.auth.models import User


class Pizza(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Tên pizza"
    )

    description = models.TextField(
        blank=True,
        verbose_name="Mô tả"
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=0,
        verbose_name="Giá"
    )

    image = models.ImageField(
        upload_to="pizza/",
        blank=True,
        null=True,
        verbose_name="Ảnh"
    )

    is_available = models.BooleanField(
        default=True,
        verbose_name="Đang bán"
    )

    class Meta:
        ordering = ["id"]
        verbose_name = "Pizza"
        verbose_name_plural = "Pizza"

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = [
        ("pending", "Chờ xử lý"),
        ("confirmed", "Đã xác nhận"),
        ("shipping", "Đang giao"),
        ("completed", "Hoàn thành"),
        ("cancelled", "Đã hủy"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="orders"
    )

    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    address = models.TextField()

    total_price = models.DecimalField(
        max_digits=12,
        decimal_places=0
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Đơn hàng #{self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )

    pizza = models.ForeignKey(
        Pizza,
        on_delete=models.PROTECT
    )

    quantity = models.PositiveIntegerField(default=1)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=0
    )

    def get_total(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.pizza.name} x {self.quantity}"