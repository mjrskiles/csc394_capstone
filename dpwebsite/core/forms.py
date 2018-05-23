from django import forms
from django.contrib.auth.forms import (UserCreationForm, UserChangeForm)
from django.contrib.auth.models import User

from dpwebsite.core.models import Profile, Courses

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=True)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        
        if commit:
            user.save()
        
        return user




class EditProfileForm(UserChangeForm):
    template_name='/something/else'
#    userLastName = forms.CharField(required=False)
    CRSE_TITLE = forms.CharField(required=False)


    class Meta:
        model = User
        fields = ('email','first_name','last_name', 'CRSE_TITLE', 'password')
            



