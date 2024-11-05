from django.shortcuts import render
from utils.portifolio.factory import make_resume


def administration(request):
    return render(request, 'portifolio/pages/resume_admin.html', context={
        'name': 'Heder Lopes'
    })


def home(request):
    return render(request, 'portifolio/pages/home.html', context={
        'name': 'Heder Lopes'
    })


def features(request):
    return render(request, 'portifolio/pages/features.html', context={
        'name': 'Heder Lopes'
    })


def contact(request):
    return render(request, 'portifolio/pages/contact.html', context={
        'name': 'Heder Lopes'
    })


def about(request):
    return render(request, 'portifolio/pages/about.html', context={
        'name': 'Heder Lopes'
    })


def resume(request):
    return render(request, 'portifolio/pages/resume.html', context={
        'resume': make_resume()
    })
