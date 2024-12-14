from django.urls import path
from .import views

urlpatterns = [
    path('get_courses/', views.list_courses, name='home'),
    path('register/<int:course_id>/', views.register_course_for_students, name='register_course'),
]

