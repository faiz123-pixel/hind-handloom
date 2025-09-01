from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Image
from .models import products
from .models import Contact
from .models import Order
from django.contrib import messages
from .forms import CheckoutForm, ProductForm,ImageForm
from django.http import HttpResponseRedirect
from django.db.models import Q


def home(request):
    return render(request,'home.html')
def home(request):
    images = Image.objects.all()  # Your slider images model
    product = products.objects.all()

    # Organize products by category
    categories = {}
    for p in product:
        category_name = p.category  # Assuming Product has a ForeignKey to Category
        if category_name not in categories:
            categories[category_name] = []
        categories[category_name].append(p)

    return render(request, 'home.html', {
        'images': images,
        'categories': categories
    })
    return render(request, 'home.html', {'images': images,'product':product })
def product_details(request,id):
    product = get_object_or_404(products,id=id)
    productss =products.objects.all()
    return render(request, 'product_details.html',{'product':product,'productss':productss})
def cart(request):
    return render(request, 'cart.html')
def about(request):
    contacts= Contact.objects.all()
    return render(request, 'about.html',{'contact':contacts})
def contact(request):
    return render(request, 'contact.html')
def shop(request):
    category_filter = request.GET.get('category')
    
    if category_filter:
        product = products.objects.filter(category=category_filter)
        categories = products.objects.values_list('category',flat=True).distinct()  # For sidebar or filter menu
    
        return render(request, 'shop.html', {
            'products': product,
            'categories': categories,
            'selected_category': category_filter
        })
    else:
        categories = products.objects.values_list('category', flat=True).distinct()
        grouped_products = {}
        for category in categories:
            grouped_products[category] = products.objects.filter(category=category)

        return render(request, 'shop.html', {
            'grouped_products': grouped_products,
            'categories': categories,
            'selected_category': None
        })

def search(request):
    query = request.GET.get('search-item')  # Get the search query from the request
    if query:
        product = products.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    else:
        product = products.objects.all()  # Show all products if no search query

    return render(request, 'search_results.html', {
        'product': product,
        'query': query,
    })

def checkout_page(request, product_id):
    product = get_object_or_404(products, id=product_id)
    
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Save the order to the database
            order = Order(
                product=product,
                name=form.cleaned_data['name'],
                mobile_number=form.cleaned_data['mobile_number'],
                email=form.cleaned_data['email'],
                pincode=form.cleaned_data['pincode'],
                home_district=form.cleaned_data['home_district'],
                address=form.cleaned_data['address'],
            )
            order.save()

            # Reduce stock after a successful purchase
            product.stock -= 1
            product.save()

            return redirect('order_confirmation', order_id=order.id)  # Redirect to confirmation page
    else:
        form = CheckoutForm()

    return render(request, 'checkout_page.html', {'form': form, 'product': product})

def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order_confirmation.html', {'order': order})


# Check if user is an admin
def is_admin(user):
    return user.is_superuser

# View to list orders (only for admin users)
@user_passes_test(is_admin)
# @user_passes_test(lambda u: u.is_superuser)
def hidden_page(request):
    if not request.session.get('is_admin_authenticated', False):
        return redirect('password_prompt')
    
    orders = Order.objects.all().order_by('-date_ordered')  # List orders, most recent first
    product = products.objects.all()
    images = Image.objects.all()

     # Handle adding products
    if request.method == 'POST' and 'name' in request.POST:
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            messages.success(request, "Product added successfully!")
        else:
            messages.error(request, "Failed to add product.")
        return redirect('hidden_page')

    # Handle image upload
    elif request.method == 'POST' and 'image' in request.FILES:
        image_form = ImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            image_form.save()
            messages.success(request, "Image uploaded successfully!")
            return redirect('hidden_page')  # Redirect to hidden admin page after image upload
        else:
            messages.error(request, "Failed to upload image.")

    else:
        product_form=ProductForm()
        image_form = ImageForm()

    return render(request, 'hidden_page.html', {
        'orders': orders,
        'products': product,
        'images': images,
        'product_form': product_form,
        'image_form': image_form,
    })

HIDDEN_PAGE_PASSWORD = "admin123"  # Use a secure method in production
# Password prompt page
@user_passes_test(lambda u: u.is_superuser)  # Only admin users can access this page
def password_prompt(request):
    if request.method == "POST":
        entered_password = request.POST.get("password")
        if entered_password == HIDDEN_PAGE_PASSWORD:
            request.session['is_admin_authenticated'] = True
            return redirect('hidden_page')
        else:
            messages.error(request, "Incorrect password!")
            return redirect('password_prompt')

    return render(request, 'password_prompt.html')

@user_passes_test(lambda u: u.is_superuser)
def update_order(request, order_id):
    order = Order.objects.get(id=order_id)
    
    if request.method == 'POST':
        # Update order fields here
        order.status = request.POST.get('status')
        order.save()
        messages.success(request, "Order updated successfully!")
        return redirect('hidden_page')
    
    return render(request, 'update_order.html', {'order': order})


@user_passes_test(lambda u: u.is_superuser)
def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        order.delete()
        messages.success(request, "Order deleted successfully!")
        return redirect('hidden_page')  # Redirect back to the hidden admin page after deletion

    return render(request, 'delete_order.html', {'order': order})


@user_passes_test(lambda u: u.is_superuser)
def update_product(request, product_id):
    product = products.objects.get(id=product_id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully!")
            return redirect('hidden_page')
        else:
            messages.error(request, "Failed to update product.")
    
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'update_product.html', {'form': form, 'product': product})

@user_passes_test(lambda u: u.is_superuser)
def delete_product(request, product_id):
    product = get_object_or_404(products, id=product_id)

    if request.method == 'POST':
        product.delete()
        messages.success(request, "Product deleted successfully!")
        return redirect('hidden_page')  # Redirect back to the hidden admin page after deletion

    return render(request, 'delete_product.html', {'product': product})

@user_passes_test(lambda u: u.is_superuser)
def delete_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)

    if request.method == 'POST':
        image.delete()
        messages.success(request, "Image deleted successfully!")
        return redirect('hidden_page')

    return render(request, 'delete_image.html', {'image': image})


