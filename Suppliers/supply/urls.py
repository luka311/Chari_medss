from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),

    # Products
    path('products/', views.products, name='products'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('delete-product/<int:id>/', views.delete_product, name='delete_product'),
    path('edit-product/<int:id>/', views.edit_product, name='edit_product'),

    # Details page
    path('services/', views.services, name='services'),
    path('orders/', views.order, name='order'),
    path('contact/', views.contact, name='contact'),

    # Auth
    path('signup/', views.signup_form, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Admin custom dashboard
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('manage_orders/', views.manage_orders, name="manage_orders"),

    # Product & Review
    path('upload-product/', views.upload_product, name='upload_product'),
    path('add-review/', views.add_review, name="add_review"),
]

# ✅ Serve media files (for images to show)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
