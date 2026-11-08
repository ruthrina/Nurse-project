from .models import Course

def nav_courses(request):
    return {
        'nav_courses': Course.objects.all()
    }