import operator
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import RestaurantUser,OurMenu,CustomerReviews, FOOD_TYPE
from .forms import RestaurantForm,CustomerReviewsForm
from django.db.models import Min
import django_filters

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = OurMenu
        fields = ['f_type']
       


def product_list(request):
    filter = ProductFilter(request.GET, queryset=OurMenu.objects.all())
    return render(request, 'restaurant/template.html', {'filter': filter})

def search(request):
       
        query = request.GET.get('search')
        r_user = RestaurantUser.objects.filter(Q(r_name__icontains = query)).first()
       
        if r_user:
           our_menu = OurMenu.objects.filter(r_name = r_user)
        else:
            all_restaurant = RestaurantUser.objects.all()
            return render(request,'restaurant/search-not-found.html',{
                'all_restaurant' :all_restaurant
            })
        return render(request,'restaurant/search-found.html',{
            'detail' : r_user,
            'rest_menu' : our_menu,

        })
        
def search_by_food(request):
       
        query = request.GET.get('search_by_food')
        food_detail = OurMenu.objects.filter(Q(food_name__icontains = query)).first()
        if food_detail:
            food_detail = OurMenu.objects.filter(Q(food_name__icontains = query)).first()
        else:
            our_menu = OurMenu.objects.all()
            return render(request,'restaurant/search-not-found_by_food.html',{
                'our_menu' : our_menu
            })


        return render(request,'restaurant/food-detail.html',{
            'food_detail' : food_detail

        })



get_val = operator.itemgetter(1)

def index(request, f_type=None):
    our_menu = OurMenu.objects.all()
    min_price = OurMenu.objects.all().aggregate(Min('food_price'))
    all_restaurant = RestaurantUser.objects.all()
    food_type = list(map(get_val, FOOD_TYPE))[:3]
 
    if f_type is None:
        filter_food = our_menu
    else:
        filter_food = OurMenu.objects.filter(f_type=f_type)
   
    
    return render(request,'index.html',{
        'our_menu' : our_menu,
        'all_restaurant' : all_restaurant,
        'min_price' :min_price.get('food_price__min'),
        'food_type' :food_type,
        'filter_food' : filter_food
    })

@login_required(login_url="/accounts/login")
def register_restaurant(request):
    form = RestaurantForm()
    if request.method == 'POST':
        form = RestaurantForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request,'restaurant/register-reservation.html',{
        'form' : form 
    })

def restaurants(request):
    all_restaurant = RestaurantUser.objects.all()
    min_price = OurMenu.objects.all().aggregate(Min('food_price'))
    return render(request,'restaurant/restaurants.html',{
        'all_restaurant' : all_restaurant,
        'min_price' :min_price.get('food_price__min')
    })

def restaurant_detail(request,rest_id):
    detail = RestaurantUser.objects.get(pk = rest_id)
    review = CustomerReviews.objects.all()
    rest_menu = detail.rest_name.all()
    min_price = detail.rest_name.all().aggregate(Min('food_price'))
    
    return render(request,'restaurant/restaurant-detail.html',{
        'detail' : detail,
        'rest_menu' :rest_menu,
        'min_price' :min_price.get('food_price__min'),
        'review' :review

         
    })


def food_detail(request,food_id):
    food_detail = OurMenu.objects.get(pk = food_id)
    return render(request,'restaurant/food-detail.html',{
          'food_detail' : food_detail

         
    })


def featured_food(request, food_by_food_filter=None):
    if food_by_food_filter:
        food = OurMenu.objects.filter(f_type=food_by_food_filter)

    our_menu = OurMenu.objects.all()
    min_price = OurMenu.objects.all().aggregate(Min('food_price'))
    all_restaurant = RestaurantUser.objects.all()
    food_type = list(map(get_val, FOOD_TYPE))[:3]
    return render(request,'index.html',{
        'our_menu' : our_menu,
        'all_restaurant' : all_restaurant,
        'min_price' :min_price.get('food_price__min'),
        'food_type' :food_type,
        'food' : food,
        
    })

def our_menu(request):
    our_menu = OurMenu.objects.all()
    min_price = OurMenu.objects.all().aggregate(Min('food_price'))
    all_restaurant = RestaurantUser.objects.all()
    food_type_list = OurMenu.objects.all().values_list('f_type')
    food_type = set(food_type_list)
 
   
   
    return render(request,'restaurant/our-menu.html',{
        'our_menu' : our_menu,
        'all_restaurant' : all_restaurant,
        'min_price' :min_price.get('food_price__min'),
        'food_type' :food_type
   
    })


### pages 
def food_gallery(request):
    food_gallery = OurMenu.objects.all()
    return render(request,'restaurant/gallery.html',{
        'food_gallery' : food_gallery
    })

def food_gallery_detail(request):
    food_gallery_detail = OurMenu.objects.all()
    return render(request,'restaurant/gallery-detail.html',{
        'food_gallery_detail' : food_gallery_detail
    })


@login_required(login_url="/accounts/login")
def customer_review(request):
    form = CustomerReviewsForm()
    if request.method == 'POST':
        form = CustomerReviewsForm(request.POST)
        
        if form.is_valid():
           
            form.save()
            return redirect('index')
    return render(request,'restaurant/customer_review.html',{
        'form' : form
    })
