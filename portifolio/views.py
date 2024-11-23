from django.shortcuts import render
from utils.portifolio.factory import make_resume
from portifolio.models import Personal, Education, Experience, Workflow, Complementary_Courses, Interests


def manager(request):
    return render(request, 'portifolio/pages/manager.html', context={
        'name': 'Heder Lopes',
        'title': 'Manager |',
    })


def home(request):
    return render(request, 'portifolio/pages/home.html', context={
        'name': 'Heder Lopes',
        'title': 'Home |',
    })


def features(request):
    return render(request, 'portifolio/pages/features.html', context={
        'name': 'Heder Lopes',
        'title': 'Features |',
    })


def contact(request):
    return render(request, 'portifolio/pages/contact.html', context={
        'name': 'Heder Lopes',
        'title': 'Contact |',

    })


def about(request):
    return render(request, 'portifolio/pages/about.html', context={
        'name': 'Heder Lopes',
        'title': 'About |',
    })


def resume(request):
    personal = Personal.objects.filter(id=1)
    education = Education.objects.all()
    experience = Experience.objects.all().order_by('-initialized_at')
    workflow = Workflow.objects.all()
    courses = Complementary_Courses.objects.all().order_by('-year', '-mounth')
    interests = Interests.objects.all()


    
    return render(request, 'portifolio/pages/resume.html', context={
        'resume': personal,
        'education': education,
        'experience': experience,
        'workflow': workflow,
        'courses':courses,
        'interests': interests,
        'title': 'Resume | Portfolio',

    })
