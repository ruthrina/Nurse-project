from django.shortcuts import render, get_object_or_404
from .models import Course

def home(request):
    # Fetch the first 6 courses to display on the homepage
    courses = Course.objects.all()[:6] 
    return render(request, 'index.html', {'courses': courses})

def courses(request):
    # Fetch all courses for the courses directory page
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})

def course_detail(request, course_slug):
    # Fetches the specific course (e.g., Bachelor) based on the URL slug
    course = get_object_or_404(Course, slug=course_slug)
    
    # Grabs all modules attached to that course
    modules = course.modules.all()
    
    context = {
        'course': course,
        'modules': modules,
    }
    return render(request, 'course_detail.html', context)

# Placeholder views for other pages
def materials(request):
    return render(request, 'materials.html')

def quizzes(request):
    return render(request, 'quizzes.html')

def contact(request):
    return render(request, 'contact.html')