from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

#account app
#redirect into account page after login


@login_required
    #def home(request):
#return render(request, 'home.html')

#
def login_success(request):
    """
        Redirects users based on whether they are in the admins group
        """
    if request.user.groups.filter(name="admin").exists():
        # user is an admin
        return redirect("admin")
    else:
        return redirect("home")



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
