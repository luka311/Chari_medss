from django.db import models
from django.contrib.auth.models import User


class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


class Product(models.Model):
    CATEGORY_CHOICES = [
        ("Hospital Consumables", "Hospital Consumables"),
        ("Disinfectants ", "Disinfectants"),
        ("Suction Machines", "Suction Machines"),
        ("Dispensing", "Dispensing"),
        ("Dental Supplies", "Dental Supplies"),
        ("Waste Management", "Waste Management"),
        ("Suctures and Surgical Blades", "Suctures and Surgical Blades"),
        ("General Examinations", "General Examinations"),
        ("Hospital Furnitures", "Hospital Furnitures"),
        ("Mobility AIDS and Psysiotherapy", "Mobility AIDS and Psysiotherapy"),
        ("Procedure test/instruments", "Procedure test/instruments"),
        ("Cathers and Collection bags", "Cathers and Collection bags"),
        ("Test Kits/strips", "Test Kits/strips"),
        ("Basic Lab Equipment", "Basic Lab Equipment"),
        ("Basic Lab Reagents", "Basic Lab Reagents"),
        ("Hospital Linens", "Hospital Linens"),

    ]

    name = models.CharField(max_length=200)
    Category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="Other")

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    phone = models.CharField(max_length=20)
    address = models.TextField()

    STATUS = (
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Delivered', 'Delivered'),
    )
    status = models.CharField(max_length=20, choices=STATUS, default="Pending")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review from {self.name}"
