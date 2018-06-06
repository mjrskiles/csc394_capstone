from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse
from dpwebsite.core.forms import (
    EditProfileForm)

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from dpwebsite.core.forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from dpwebsite.core.path_finder import PathFinder
from .forms import ReportForm
from .forms import SavedPathForm
from dpwebsite.core.models import CorePath
from dpwebsite.core.models import CoreCourses
from django.utils.crypto import get_random_string
from collections import defaultdict
from .forms import ClassSearchForm
from dpwebsite.core.models import AuthUserGroups




def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
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
            form.save()
            return redirect(reverse('view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}

        return render(request, 'edit_profile.html', args)


def login_success(request):
    isSuper = None
    isStaff = None
    if request.user.is_authenticated:
        isSuper = request.user.is_superuser
        isStaff = request.user.is_staff
    print(isSuper)
    print(isStaff)
    if isSuper:
        return redirect(reverse('ADMIN_URL'))
    else:
        return redirect(reverse('home'))


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })


def report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            major = int(form.cleaned_data['select_major_'])
            concentration = int(form.cleaned_data['select_concentration_'])
            num_per_term = int(form.cleaned_data['select_number_of_courses_per_term_'])
            temp = PathFinder()
            myreturn = temp.find_shortest_path(major,concentration,num_per_term)
            #form.report_table.
            quarters = ["0", "1", "2", "3"]
            quarterNames = ["Fall", "Winter", "Spring", "Summer"]
            n = 0
            q = 1
            pathID = get_random_string(20,'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
            for i in range(len(myreturn)):
                for c in myreturn[i]:
                    toSave = CorePath()
                    toSave.courseid = c.id
                    toSave.pathquarter = quarters[n]
                    toSave.pathsteps = q
                    toSave.user_id = request.user.id
                    toSave.path_id = pathID
                    toSave.save()
                    q += 1
                n += 1
                if n > len(quarters) - 1:
                    n = 0
            return render(request, 'report.html', {
                'formDatas': myreturn,
            })
    else:
        form = ReportForm()
    return render(request, 'report.html', {'form': form})


def get_saved_paths(request):
        if (request.POST.get('delete_path')):
            CorePath.objects.filter(path_id=request.POST.get('delete_path')).delete()
            formset = CorePath.objects.filter(user_id=request.user.id).values_list('path_id', flat=True).distinct()
            return render(request, 'saved_paths_page.html', {'formset': formset})
        elif (request.POST.get('view_path')):
            request.session['curPathID'] = request.POST.get('view_path')
            return redirect(reverse('single_path'))
        else:
            formset = CorePath.objects.filter(user_id=request.user.id).values_list('path_id', flat=True).distinct()
            return render(request, 'saved_paths_page.html', {'formset': formset})


def single_path(request):
    if request.POST.get('returnFromPath'):
        return redirect(reverse('saved_paths'))
    else:
        pathID = request.session['curPathID']
        myPath = CorePath.objects.filter(path_id=pathID).order_by('pathsteps')
        myList = []
        curList = []
        lastPathQuarter = 0
        curTerm = 1
        for item in myPath:
            curCourse = CoreCourses.objects.filter(id=item.courseid)[0]
            if lastPathQuarter == item.pathquarter:
                curList.append((curCourse.CRSE_SUBJECT +" "+str(curCourse.CRSE_NBR)))
            else:
                myList.append(curList)
                curList = []
                curList.append((curCourse.CRSE_SUBJECT +" "+str(curCourse.CRSE_NBR)))
            lastPathQuarter = item.pathquarter
        return render(request,'single_path.html', {'form': myList})


def class_search(request):
    toReturn = []
    print("Wee")
    if request.POST.get('classSearch'):
        searchChoice = int(request.POST.get('select_search_choice'))
        searchText = request.POST.get('search_text')
        print(searchChoice)
        print(type(searchChoice))
        print(type(searchText))
        if searchChoice == 0:
            #id
            returned = CoreCourses.objects.filter(id = int(searchText))
            for item in returned:
                toReturn.append(item)
        elif searchChoice == 1:
            #title
            returned = CoreCourses.objects.filter(CRSE_TITLE = searchText)
            for item in returned:
                toReturn.append(item)
        elif searchChoice == 2:
            #description
            returned = CoreCourses.objects.filter(CRSE_DESCRIPTION = searchText)
            for item in returned:
                toReturn.append(item)
        elif searchChoice == 3:
            #subject
            returned = CoreCourses.objects.filter(CRSE_SUBJECT = searchText)
            for item in returned:
                toReturn.append(item)
        elif searchChoice == 4:
            #course number
            returned = CoreCourses.objects.filter(CRSE_NBR = int(searchText))
            for item in returned:
                toReturn.append(item)
    print(toReturn)
    if request.method == 'POST':
        form = ClassSearchForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = ClassSearchForm()
    return render(request,'class_search.html', { 'form': form, 'classes': toReturn})


def faculty_page(request):
    AUG = AuthUserGroups.objects.filter(user= request.user.id).values()
    myid = 0
    myStudents = []
    for item in AUG:
        myid= int(item['id'])

    AUG2 = AuthUserGroups.objects.values()
    for items in AUG2:
        if int(items['id']) == myid:
            if int(items['user_id']) != request.user.id:
                myStudents.append(int(items['user_id']))
    formset = CorePath.objects.filter(user_id=myStudents[0]).values_list('path_id', flat=True).distinct()

    return render(request,'facultyPage.html',{'students': myStudents,'paths': formset })
