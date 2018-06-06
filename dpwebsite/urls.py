"""dpwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from dpwebsite.core import views as core_views
from django.views.generic.base import RedirectView
from dpwebsite.core import views

#admin_url = 'login/?next=/admin/'
#/admin/login/?next=/admin/

ADMIN_URL = 'https://docs.djangoproject.com/en/dev/ref/contrib/admin/'

urlpatterns = [
    url(r'^$', auth_views.login, {'template_name': 'login.html'}, name='main'),
    url(r'^home/$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^faculty/$', views.faculty_page, name='faculty'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^profile/$', core_views.view_profile, name='view_profile'),
    url(r'^profile/(?P<pk>\d+)/$', core_views.view_profile, name='view_profile_with_pk'),
    #           url(r'^profile/(?P<pk>\d+)/$', core_views.view_profile, name='view_profile_with_pk'),
    url(r'^profile/edit/$', core_views.edit_profile, name='edit_profile'),
    url(r'^schedule/$', auth_views.login, {'template_name': 'schedule.html'}, name='schedule'),
    url(r'^report/$', views.report, name='report'),
    url(r'^report2/$', auth_views.login, {'template_name': 'report2.html'}, name='report2'),

    # url(r'^login_success/$', core_views.login_success, name='login_success'),
    url(r'^login_success/$', core_views.login_success, name='login_success'),
    url(r'^admin/', admin.site.urls),
    url('^admin/$', RedirectView.as_view(url=ADMIN_URL), name='ADMIN_URL'),
    url(r'^profile/password/$', core_views.change_password, name='change_password'),
    url(r'^saved_paths/$', views.get_saved_paths, name="saved_paths"),
    url(r'^single_path/$', views.single_path, name="single_path"),
    url(r'^class_search/$', views.class_search, name="class_search"),

            
]
