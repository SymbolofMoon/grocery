from django import forms 
from .models import Item 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  
  
# creating a form 
class ListForm(forms.ModelForm): 
  
    # create meta class 
    class Meta: 
        # specify model to be used 
        model = Item 
        
        # specify fields to be used 
        fields = ['name','quantity','status','added_date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'added_date': forms.DateInput(attrs={'class': 'form-control datepicker'})
        }

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
