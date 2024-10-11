from django.contrib import admin
from .models import Image
from .models import products
from .models import Contact
from .models import Order


# Register your models here.

@admin.register(Image)
class imagesadmin(admin.ModelAdmin):
    list_display =['title','image']
@admin.register(products)
class productsadmin(admin.ModelAdmin):
    list_display =['name','price','description','color','image','stock']
    search_fields = ['name']
    list_filter = ['stock']
@admin.register(Contact)
class productsadmin(admin.ModelAdmin):
    list_display =['phone_number','email','address']
@admin.register(Order)
class productsadmin(admin.ModelAdmin):
    list_display =['product','name','mobile_number','email','home_district','address','date_ordered']
    search_fields = ['name','mobile_number']
    list_filter = ['date_ordered']
