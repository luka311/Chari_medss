from django.contrib import admin
from .models import ContactMessage, Product, Order, Review


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "created_at")
    search_fields = ("name", "email", "phone")
    list_filter = ("created_at",)
    readonly_fields = ("name", "email", "phone", "message", "created_at")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price")
    search_fields = ("name", "category")
    list_filter = ("category",)
    list_editable = ("price",)  # allow changing price quickly


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "product", "quantity", "status", "date")
    list_filter = ("status", "date")
    search_fields = ("user__username", "product__name")
    list_editable = ("status",)  # change order status from admin table
    readonly_fields = ("user", "product", "quantity", "phone", "address", "date")


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "created_at")
    search_fields = ("name", "user__username")
    list_filter = ("created_at",)
    readonly_fields = ("name", "message", "user", "created_at")
