from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse
from dpwebsite.core.forms import (
    RegistrationForm,
    EditProfileForm)

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required




def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
           
            form.save()
        
            return redirect(reverse('login'))
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})


def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
#            user =

            form.save()
#            user.profile.userLastName = form.cleaned_data.get('userLastName')
#            user.save()
            return redirect(('view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        
        return render(request, 'edit_profile.html', args)

