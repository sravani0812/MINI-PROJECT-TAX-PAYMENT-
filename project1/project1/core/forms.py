from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import *

class CustomerForm(ModelForm):
	class Meta:
		model = Donor
		fields = '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'Aadhar_Card', 'Pan_Card','Income','pdf', 'image')

