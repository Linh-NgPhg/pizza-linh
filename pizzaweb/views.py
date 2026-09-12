from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Pizza
from django.contrib.auth import login, logout
from .forms import RegisterForm


def home(request):
    pizzas = Pizza.objects.filter(
        is_available=True
    )

    return render(
        request,
        "home.html",
        {
            "pizzas": pizzas
        }
    )


def logout_view(request):
    logout(request)
    return redirect("login")


def cart(request):
    cart = request.session.get("cart", {})

    cart_items = []
    total = 0

    for pizza_id, quantity in cart.items():

        pizza = get_object_or_404(
            Pizza,
            id=pizza_id,
            is_available=True
        )

        item_total = pizza.price * quantity
        total += item_total

        cart_items.append({
            "pizza": pizza,
            "quantity": quantity,
            "item_total": item_total,
        })

    return render(
        request,
        "cart.html",
        {
            "cart_items": cart_items,
            "total": total,
        }
    )


def add_to_cart(request, pizza_id):

    pizza = get_object_or_404(
        Pizza,
        id=pizza_id,
        is_available=True
    )

    cart = request.session.get("cart", {})

    pizza_id = str(pizza.id)

    cart[pizza_id] = cart.get(pizza_id, 0) + 1

    request.session["cart"] = cart

    messages.success(
        request,
        f"Đã thêm {pizza.name} vào giỏ hàng."
    )

    return redirect("home")


def remove_from_cart(request, pizza_id):

    cart = request.session.get("cart", {})

    pizza_id = str(pizza_id)

    if pizza_id in cart:
        del cart[pizza_id]

    request.session["cart"] = cart

    return redirect("cart")


def register(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(
                request,
                user
            )

            return redirect("home")

    else:

        form = RegisterForm()

    return render(
        request,
        "register.html",
        {
            "form": form
        }
    )
def payment_success(request):
    # Thanh toán thành công → xóa giỏ hàng
    request.session["cart"] = {}

    return redirect("home")


def payment_cancel(request):
    # Hủy thanh toán → giữ nguyên giỏ hàng
    return redirect("cart")