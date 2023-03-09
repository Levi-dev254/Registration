from django.shortcuts import render, redirect
from django.contrib import messages
from.forms import UserregistrationForm
from django.contrib.auth.decorators import login_required
from .models import Product


def register(request):
    if request.method == 'POST':
        form = UserregistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account created successfully!')
            return redirect('register')
    else:
        form = UserregistrationForm()
    return render(request,'register.html',{'form' : form})

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def add_product(request):
    # Check if the form submitted has a method post
    if request.method == "POST":

        # Start receiving data from the form
        p_name = request.POST.get('jina')
        p_quantity = request.POST.get('kiasi')
        p_price = request.POST.get('bei')

        # Finally save the data in our table called products
        product = Product(prod_name = p_name,prod_quantity=p_quantity,
                          prod_price=p_price)

        product.save()
        # Redirect back with a success message
        messages.success(request, 'Product saved successfully')
        return redirect('add-product')
    return render(request, 'addproducts.html')


@login_required
def view_products(request):
    # Select all the products to be displayed
    products = Product.objects.all()
    return render(request, 'products.html', {'products':products})

@login_required
def delete_product(request, id):
    # Fetch the product to be deleted
    product = Product.objects.get(id=id)
    # Delete the product
    product.delete()
    # Redirect back to products page with a success message
    messages.success(request,'Product deleted successfully')
    return redirect('products')

@login_required
def update_product(request,id):
    # Fetch the product to be updated
    product = Product.objects.get(id=id)
    #  Check if the method submitted has a method post
    if request.method == "POST":
     # Receive data from the form
        update_name = request.POST.get('jina')
        update_quantity = request.POST('kiasi')
        update_price = request.POST.GET('bei')

    # Update the product with the received update data
        product.prod_name = update_name

        product.prod_quantity = update_quantity

        product.prod_price = update_price

    # Return the data back to the database and redirect back
    # to products page with a success massage
    product.save()
    messages.success(request, 'Product updated successfully')

    return render(request, 'updateproduct.html',{'product':product})

@login_required
def payment(request, id):
    # select the product to be paid
    product = Product.objects.get(id=id)
    return render(request, 'payment.html', {'product' : product})
