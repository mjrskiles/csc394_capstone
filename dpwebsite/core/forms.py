from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    # userID = forms.CharField(max_length=50)
    #userName = forms.CharField(max_length=50)
    #userPassword = forms.CharField(max_length=50)
    userEmail = forms.EmailField(max_length=50)
    userFirstName = forms.CharField(max_length=50)
    userLastName = forms.CharField(max_length=50)
#    userDegree = forms.CharField(max_length=25)

    class Meta:
        model = User
        fields = ('username', 'userFirstName', 'userLastName', 'userEmail','password1', 'password2',)

