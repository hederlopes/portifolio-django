from django.urls import path
from portifolio.views import home, features, contact, about, resume


urlpatterns = [
    path('', home),
    path('features/', features),
    path('contact/', contact),
    path('about/', about),
    path('resume/', resume),
]
