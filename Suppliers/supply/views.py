from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .decorators import admin_required
from .models import Product, Order, Review
from .forms import ContactForm, ProductForm, ReviewForm


# ---------------------- USER VIEWS ----------------------

@login_required
def home(request):
    products = Product.objects.all()
    return render(request, "home.html", {"products": products})


@login_required
def products(request):
    items = Product.objects.all()
    return render(request, 'products.html', {'items': items})


@login_required
def services(request):
    return render(request, 'services.html')


@login_required
def order(request):
    products = Product.objects.all()

    if request.method == "POST":
        product_id = request.POST.get("product")
        quantity = request.POST.get("quantity")
        phone = request.POST.get("phone")
        address = request.POST.get("address")

        product = Product.objects.get(id=product_id)

        Order.objects.create(
            user=request.user,
            product=product,
            quantity=quantity,
            phone=phone,
            address=address
        )

        message = f"Hello Charis MedSuppliers, I want to order:\nProduct: {product.name}\nQty: {quantity}\nPhone: {phone}\nDelivery: {address}"
        whatsapp_url = f"https://wa.me/254741188424?text={message.replace(' ', '%20')}"

        return redirect(whatsapp_url)

    return render(request, 'order.html', {"products": products})


@login_required
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # ✅ Save message to DB
            messages.success(request, "✅ Your message has been sent successfully! We will contact you soon.")
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {"form": form})

@login_required
def add_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.name = request.user.username
            review.save()
            messages.success(request, "Thank you for your feedback!")
            return redirect('home')
    else:
        form = ReviewForm()

    return render(request, "add_review.html", {"form": form})


@login_required
def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, "product_detail.html", {"product": product})


# ---------------------- ADMIN VIEWS ----------------------

@login_required
@admin_required
def admin_dashboard(request):
    orders = Order.objects.all()
    reviews = Review.objects.all()
    products = Product.objects.all()

    return render(request, "admin_dashboard.html", {
        "orders": orders,
        "reviews": reviews,
        "products": products
    })


@login_required
@admin_required
def manage_orders(request):
    orders = Order.objects.all().order_by('-date')

    if request.method == "POST":
        order_id = request.POST.get("order_id")
        new_status = request.POST.get("status")

        order = Order.objects.get(id=order_id)
        order.status = new_status
        order.save()

        messages.success(request, "Order updated successfully!")
        return redirect('manage_orders')

    return render(request, "manage_orders.html", {"orders": orders})


@login_required
@admin_required
def upload_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Product added successfully!")
            return redirect('products')
    else:
        form = ProductForm()

    return render(request, "upload_product.html", {"form": form})


@login_required
@admin_required
def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    messages.success(request, "Product deleted successfully!")
    return redirect('products')


@login_required
@admin_required
def edit_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully!")
            return redirect('products')
    else:
        form = ProductForm(instance=product)

    return render(request, 'edit_product.html', {"form": form})


# ---------------------- AUTH ----------------------

def signup_form(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()

    # corrected template name
    return render(request, "signup_form.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('admin_dashboard')
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect('login')
