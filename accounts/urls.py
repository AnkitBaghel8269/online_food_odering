from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import LoginView

urlpatterns = [
    # path('',views.home, name = 'home'),
    path('register/', views.register , name  = 'register'),
    path('login/',auth_views.LoginView.as_view(template_name = 'accounts/login.html'), name = 'login'),
    path('logout/',auth_views.LogoutView.as_view(), name = 'logout'),
    # path('accounts/user_prifile/',views.profile_page, name = 'profile_page'),
    
    
]
 