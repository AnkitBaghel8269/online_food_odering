from django import forms
from .models import CustomerUser,ContectUs
PRODUCT_CHOICE = [
   (i,str(i)) for i in range(1,21)
]

class AddquantityForm(forms.Form):
    quantity = forms.TypedChoiceField(choices = PRODUCT_CHOICE,coerce = int)



class CustomerForm(forms.ModelForm):
    

    class Meta:
      model = CustomerUser
      fields = '__all__'


class ContectUsForm(forms.ModelForm):
    

    class Meta:
      model = ContectUs
      fields = '__all__'