from django import forms
from .models import RestaurantUser,OurMenu,CustomerReviews

class RestaurantForm(forms.ModelForm):

    class Meta:
        model =  RestaurantUser
        fields = '__all__'



    
class OurMenuForm(forms.ModelForm):

    class Meta:
        model =  OurMenu
        fields = '__all__'



class CustomerReviewsForm(forms.ModelForm):

    class Meta:
        model =  CustomerReviews
        fields = '__all__'