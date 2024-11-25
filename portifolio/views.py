from django.shortcuts import get_list_or_404, get_object_or_404, render
from portifolio.models import Personal, Education, Experience, Workflow, Complementary_Courses, Interests, Message  # noqa E501


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


def blog(request):
    blog = Message.objects.filter(
        is_published=True,
    ).order_by('created_at')
    return render(request, 'portifolio/pages/blog.html', context={
        'blog': blog,
        'title': 'Blog |',

    })


def post(request, id):
    post = get_object_or_404(Message.objects.filter(pk=id, is_published=True))
    return render(request, 'portifolio/pages/blog-view.html', context={
        'post': post,
        'title': 'Post |',

    })


def about(request):
    return render(request, 'portifolio/pages/about.html', context={
        'name': 'Heder Lopes',
        'title': 'About |',
    })


def resume(request):
    personal = Personal.objects.filter(id=1)
    education = Education.objects.all()
    experience = Experience.objects.filter(
        visible=True,
    ).order_by('-initialized_at')
    workflow = Workflow.objects.all()
    courses = Complementary_Courses.objects.all().order_by('-year', '-mounth')
    interests = Interests.objects.all()

    return render(request, 'portifolio/pages/resume.html', context={
        'resume': personal,
        'education': education,
        'experience': experience,
        'workflow': workflow,
        'courses': courses,
        'interests': interests,
        'title': 'Resume | Portfolio',

    })
