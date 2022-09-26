from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models
from django import forms



class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class DiseaseForm(forms.ModelForm):   
    class Meta:
        model = models.Disease
        fields = ('name', 'identified_by', 'desc')

class MedicineForm(forms.ModelForm):
    class Meta:
        model = models.Medicine
        fields = ('name', 'desc')