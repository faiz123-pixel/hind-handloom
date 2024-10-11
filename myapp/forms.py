# products/forms.py
from django import forms
from .models import products, Image

class ProductForm(forms.ModelForm):
    class Meta:
        model = products
        fields = ['name', 'price','description','color', 'stock', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'image']

class CheckoutForm(forms.Form):
    name = forms.CharField(max_length=100, label="Full Name")
    mobile_number = forms.CharField(max_length=15, label="Mobile Number")
    email = forms.EmailField(max_length=254, label="Email") 
    pincode = forms.CharField(max_length=6, label="Pincode")
    home_district = forms.CharField(max_length=100, label="District")
    address = forms.CharField(max_length=300, label="Address")
