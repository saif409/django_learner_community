"""reportlogin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_home, name="admin_home"),
    path('login/', views.userlogin, name="login"),
    path('logout/', views.user_logout, name="user_logout"),
    path('surveyor-list/', views.surveyor_list, name="surveyor_list"),
    path('survey-list/', views.survey_list, name="survey_list"),
    path('add-new-survey/', views.add_new_survey, name="add_new_survey"),
    path('remove-survey/<int:id>/', views.remove_survey, name="remove_survey"),
    path('update-survey/<int:id>/', views.update_survey, name="update_survey"),
    path('add-new-country', views.add_new_country, name="add_new_country"),
    path('add-new-division', views.add_new_division, name="add_new_division"),




]
