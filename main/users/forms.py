from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from main.models import Reservation

class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['computer_number', 'duration_time', 'description']