from django.shortcuts import render, redirect
from restaurant.models import OurMenu
from django.contrib.auth.decorators import login_required
from .cart import Cart
from .forms import ContectUsForm, CustomerForm

@login_required(login_url="/accounts/login")
def cart_add(request, id):
    cart = Cart(request)
    product = OurMenu.objects.get(id=id)
    cart.add(product=product)
    
    return redirect("food_detail", product.id)


@login_required(login_url="/accounts/login")
def item_clear(request, id):
    cart = Cart(request)
    product = OurMenu.objects.get(id=id)
    cart.remove(product)
    return redirect("food_detail", product.id)


@login_required(login_url="/accounts/login")
def item_increment(request, id):
    cart = Cart(request)
    product = OurMenu.objects.get(id=id)
    cart.add(product=product)
    return redirect("food_detail", product.id)


@login_required(login_url="/accounts/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = OurMenu.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("food_detail", product.id)


@login_required(login_url="/accounts/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("index")


@login_required(login_url="/accounts/login")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')




def customer_detail(request):
    form = CustomerForm()
    if request.method == 'POST': 
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'order/customer_detail.html',{
        'form' : form
    }) 

def thankyou(request):
    return render(request,'order/thankyou.html')



def contect_us(request):
    form = ContectUsForm()
    if request.method == 'POST': 
        form = ContectUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'order/contect_us.html',{
        'form' : form
    }) 




