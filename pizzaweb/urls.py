from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    # Trang chủ
    path("", views.home, name="home"),

    # Giỏ hàng
    path("cart/", views.cart, name="cart"),
    path(
        "cart/add/<int:pizza_id>/",
        views.add_to_cart,
        name="add_to_cart",
    ),
    path(
        "cart/remove/<int:pizza_id>/",
        views.remove_from_cart,
        name="remove_from_cart",
    ),

    # Đăng nhập
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="login.html"
        ),
        name="login",
    ),

    # Đăng xuất
    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),

    # Đăng ký
    path(
        "register/",
        views.register,
        name="register",
    ),

    # Thanh toán
    path(
    "payment/success/",
    views.payment_success,
    name="payment_success",
    ),

    path(
    "payment/cancel/",
    views.payment_cancel,
    name="payment_cancel",
    ),
]
