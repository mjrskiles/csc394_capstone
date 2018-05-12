from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    #birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    userID = forms.CharField(max_length=50)
    userName = forms.CharField(max_length=50)
    #userPassword = forms.CharField(max_length=50)
    userEmail = forms.CharField(max_length=50)
    userAddress = forms.CharField(max_length=100)
    userCity = forms.CharField(max_length=30)
    userZip = forms.IntegerField()
    userState = forms.CharField(max_length=2)
    userFirstName = forms.CharField(max_length=50)
    userLastName = forms.CharField(max_length=50)
    userDegree = forms.CharField(max_length=25)

    class Meta:
        model = User
        fields = ('id', 'userName', 'userEmail','password1', 'password2', 'userAddress' , 'userCity', 'userZip', 'userState', 'userFirstName', 'userLastName', 'userDegree')
