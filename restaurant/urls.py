from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
        path('', views.index , name  = 'index'),
        path('restaurant/register_restaurant/',views.register_restaurant, name = 'register_restaurant'),
        path('restaurant/all_restaurants/',views.restaurants, name = 'all_restaurants'),
        path('restaurant/restaurant_detail/<int:rest_id>/',views.restaurant_detail, name = 'restaurant_detail'),
        path('restaurant/food_detail/<int:food_id>/',views.food_detail, name = 'food_detail'),
        path('restaurant/our_menu/',views.our_menu, name = 'our_menu'),
        path('restaurant/search/',views.search, name = 'search_results'),
         path('restaurant/search_by_food_results/',views.search_by_food, name = 'search_by_food_results'),

        ##pages
        path('restaurant/food_gallery/',views.food_gallery, name  = 'food_gallery'),
        path('restaurant/customer/reviews/',views.customer_review, name  = 'review'),
        path('restaurant/food_gallery_detail/',views.food_gallery_detail, name  = 'food_gallery_detail'),
        path('feature/<str:food_by_food_filter>/', views.featured_food, name='featured_food'),
        path('product/list/', views.product_list, name='productlist'),

    
] 


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)