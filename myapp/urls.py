from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='home'),
    path('product/<int:id>/',views.product_details, name='product_details'),
    path('cart/', views.cart, name='cart'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),

    path('checkout_page/<int:product_id>/', views.checkout_page, name='checkout_page'),
    path('order-confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),

    path('hidden_page', views.hidden_page, name='hidden_page'),
    path('password_prompt', views.password_prompt, name='password_prompt'),
    path('update_order/<int:order_id>/', views.update_order, name='update_order'),
    path('delete_order/<int:order_id>/', views.delete_order, name='delete_order'),
    path('update_product/<int:product_id>/', views.update_product, name='update_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('delete_image/<int:image_id>/', views.delete_image, name='delete_image'),
    
]
