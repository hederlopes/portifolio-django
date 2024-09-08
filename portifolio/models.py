from django.db import models
from django.contrib.auth.models import User


class Personal(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    age = models.IntegerField()
    marital_status = models.CharField(max_length=45)
    cover = models.ImageField(upload_to='portifolio/covers/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )


class Address(models.Model):
    street = models.CharField(max_length=45)
    number = models.CharField(max_length=45)
    neighborhood = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    zipcode = models.CharField(max_length=45)
    complement = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=False)
    personal_id = models.ForeignKey(
        Personal, on_delete=models.SET_NULL, null=True
    )


class Contact(models.Model):
    type = models.CharField(max_length=45)
    descrption_contact = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=False)
    personal_id = models.ForeignKey(
        Personal, on_delete=models.SET_NULL, null=True
    )


class Complementary_Courses(models.Model):
    course = models.CharField(max_length=100)
    instituition = models.CharField(max_length=45)
    duration = models.IntegerField()
    mounth = models.CharField(max_length=45)
    year = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=False)
    personal_id = models.ForeignKey(
        Personal, on_delete=models.SET_NULL, null=True
    )


class Education(models.Model):
    university = models.CharField(max_length=45)
    academic_title = models.CharField(max_length=45)
    course = models.CharField(max_length=45)
    initialized_at = models.DateField(auto_now=False)
    finished_at = models.DateField(auto_now=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=False)
    personal_id = models.ForeignKey(
        Personal, on_delete=models.SET_NULL, null=True
    )


class Experience(models.Model):
    company = models.CharField(max_length=45)
    positions = models.CharField(max_length=45)
    initialized_at = models.DateField(auto_now=False)
    finished_at = models.DateField(auto_now=False)
    reponsabilities = models.TextField()
    visible = models.BooleanField(True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=False)
    personal_id = models.ForeignKey(
        Personal, on_delete=models.SET_NULL, null=True
    )


class Interests(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=False)
    personal_id = models.ForeignKey(
        Personal, on_delete=models.SET_NULL, null=True
    )


class Skills(models.Model):
    skill_name = models.CharField(max_length=45)
    icon = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=False)
    personal_id = models.ForeignKey(
        Personal, on_delete=models.SET_NULL, null=True
    )
