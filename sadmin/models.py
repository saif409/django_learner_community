from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver


# Create your models here.
ROLE_CHOICES = (
    (1, 'Admin'),
    (2, 'Supervisor'),
    (3, 'User'),
)


STATUS_CHOICES = (
    (1, 'Active'),
    (2, 'InActive'),
    (3, 'Rejected'),
)


class Surveyor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='user_info')
    address = models.CharField(max_length=200)
    profile_picture = models.ImageField()
    country = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    sub_district = models.CharField(max_length=100)
    email = models.CharField(max_length=100,null=True, blank=True)
    graduation_subject = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    skills = models.CharField(max_length=200)
    area = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    description = models.TextField()
    designation = models.CharField(max_length=100)
    experience = models.CharField(max_length=200)
    role = models.IntegerField(choices=ROLE_CHOICES, null=True, default=3)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    status = models.IntegerField(choices=STATUS_CHOICES, null=True, default=2)

    def __str__(self):
        return str(self.user)


class Survey(models.Model):
    surveyor = models.CharField(max_length=200)
    contact_person_name = models.CharField(max_length=200)
    contact_person_email = models.CharField(max_length=200)
    contact_person_phone = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    company_address = models.CharField(max_length=200)
    company_email = models.CharField(max_length=200)
    description = models.TextField()
    created_at =models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.company_name


class Country(models.Model):
    country_name = models.CharField(max_length=200)

    def __str__(self):
        return self.country_name


class Division(models.Model):
    division_name = models.CharField(max_length=200)

    def __str__(self):
        return self.division_name


class District(models.Model):
    district_name = models.CharField(max_length=200)

    def __str__(self):
        return self.district_name


class SubDistrict(models.Model):
    sub_district_name = models.CharField(max_length=200)

    def __str__(self):
        return self.sub_district_name