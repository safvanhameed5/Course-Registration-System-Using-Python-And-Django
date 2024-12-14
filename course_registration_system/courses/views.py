from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Course, Student
from .forms import StudentForm

def list_courses(request):
    courses = Course.objects.all()

    context_data = {
        "courses": courses
    }

    return render(request, 'courses/list_courses.html', context=context_data)

def register_course_for_students(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if course.current_enrolled >= course.maximum_capacity:
        return HttpResponse("<h1>Registration closed: Course is full.</h1><a href='/get_courses'>Back To Course</a>", status=403)

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']

            student, created = Student.objects.get_or_create(email=email, defaults={'name': name})

            if not created and student.name != name:
                student.name = name
                student.save()

            if student.enrolled_courses.filter(id=course.id).exists():
                return HttpResponse("<h1>You are already registered for this course.</h1><a href='/get_courses'>Back To Course</a>", status=403)

            student.enrolled_courses.add(course)

            course.current_enrolled += 1
            course.save()

            return redirect('/get_courses')
    else:
        form = StudentForm()

    return render(request, 'courses/register_courses.html', {'form': form, 'course': course})
