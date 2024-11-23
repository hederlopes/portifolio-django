from django.urls import path
from . import views

app_name = 'portifolio'


urlpatterns = [
    path('', views.home, name="home"),
    path('manager/', views.manager, name="manager"),
    path('features/', views.features, name="features"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('resume/', views.resume, name="resume"),
]
