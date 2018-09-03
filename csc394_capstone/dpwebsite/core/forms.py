from django import forms
from django.contrib.auth.forms import (UserCreationForm, UserChangeForm)
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    #username = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=30, required=True, help_text='First Name Required!')
    last_name = forms.CharField(max_length=30, required=True, help_text='Last Name Required!')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class EditProfileForm(UserChangeForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    email.widget.attrs.update(size='40')


    class Meta:
        model = User
        exclude = ('password',)
        fields = ('first_name', 'last_name', 'email')


class ReportForm(forms.Form):
    majorChoices = ((0, 'CS'), (1, 'IS'))
    concentrationChoices = ((0, 'CS - Software and System Dev'), (1, 'CS - Theory'), (2, 'CS - Data Science'),
                            (3, 'CS - Database Systems'), (4, 'CS - Artificial Intelligence'),
                            (5, 'CS - Software Engineering'), (6, 'CS - Game - Real Time'),
                            (7, 'CS - Human - Computer Interaction'), (0, 'IS - Business Analysis'),
                            (1, 'IS - Business Intel'), (2, 'IS- DB Admin'),
                            (3, 'IS - IT Enterprise'), (4, 'IS - Standard'))
    numOfCoursesTakenChoices = ((1, '1'), (2, '2'), (3, '3'))

    select_major_ = forms.ChoiceField(choices=majorChoices)
    select_concentration_ = forms.ChoiceField(choices=concentrationChoices)
    select_number_of_courses_per_term_ = forms.ChoiceField(choices=numOfCoursesTakenChoices)


class SavedPathForm(forms.Form):
    path_id = forms.CharField(max_length=20)

class ClassSearchForm(forms.Form):
    #id, title, description, subject, number
    searchChoices = ((0, 'Course ID'), (1, 'Course Title'), (2, 'Course Description'),
                     (3, 'Course Subject'), (4, 'Course Number'))
    search_text = forms.CharField(max_length=50)
    select_search_choice = forms.ChoiceField(choices=searchChoices)




