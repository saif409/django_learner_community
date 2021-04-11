from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.core.paginator import Paginator
from django.utils.decorators import method_decorator
from django.views import View
from.models import Surveyor, Survey
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail

# Create your views here.


def userlogin(request):
    if request.user.is_authenticated:
        return redirect('admin_home')
    else:
        if request.method == "POST":
            user = request.POST.get('user', )
            password = request.POST.get('pass', )
            auth = authenticate(request, username=user, password=password)
            if auth is not None:
                login(request, auth)
                return redirect('admin_home')
            else:
                messages.add_message(request, messages.ERROR, 'Username or password mismatch!')
    return render(request, "login.html")


def user_logout(request):
    logout(request)
    return redirect('login')


def admin_home(request):
    if request.user.is_authenticated:
        total_data_collector = Surveyor.objects.all().count()
        context={
            "isact_home":"active",
            "total_data_collector":total_data_collector,
            "title": "Dashboard",

        }
        return render(request, "admin_home.html", context)
    else:
        return redirect('login')


def surveyor_list(request):
    user_obj = Surveyor.objects.all()[::-1]
    context={
        "isact_surveyorlist": "active",
        "user":user_obj
    }
    return render(request, "user/surveyor_list.html", context)


def add_new_user(request):
    return render(request, "user/add_new_user.html")


def survey_list(request):
    survey_obj = Survey.objects.all()
    context={
        "isact_surveylist":"active",
        "survey":survey_obj
    }
    return render(request, "survey/survey_list.html",context)


def add_new_survey(request):
    if request.method == "POST":
        surveyor = request.user
        contact_person_name = request.POST.get("contact_person_name")
        contact_person_email = request.POST.get("contact_person_email")
        contact_person_phone = request.POST.get("contact_person_phone")
        company_name = request.POST.get("company_name")
        company_address = request.POST.get("company_address")
        company_email = request.POST.get("company_email")
        description = request.POST.get("description")

    return render(request, "survey/add_new_survey.html")