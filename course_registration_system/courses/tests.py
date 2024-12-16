from django.test import TestCase
from .models import Course, Student
from django.urls import reverse
from .forms import StudentForm

class CourseModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title="Python 101",
            description="An introductory Python course",
            maximum_capacity=30
        )

    def test_course_str(self):
        """Test string representation of Course model."""
        self.assertEqual(str(self.course), "Python 101")


class StudentModelTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            name="John Doe",
            email="john.doe@example.com"
        )

    def test_student_str(self):
        """Test string representation of Student model."""
        self.assertEqual(str(self.student), "John Doe")

class CourseViewTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title="Python 101",
            description="An introductory Python course",
            maximum_capacity=30
        )

    def test_list_courses_view(self):
        """Test that the list_courses view returns a 200 response and uses the correct template."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/list_courses.html')

    def test_register_course_view(self):
        """Test registering for a course with an empty form."""
        response = self.client.get(reverse('register_course', args=[self.course.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/register_courses.html')

class StudentFormTest(TestCase):
    def test_student_form_valid(self):
        """Test form validation with valid data."""
        form = StudentForm(data={'name': 'John Doe', 'email': 'john.doe@example.com'})
        self.assertTrue(form.is_valid())

    def test_student_form_invalid(self):
        """Test form validation with invalid data."""
        form = StudentForm(data={'name': '', 'email': 'not-an-email'})
        self.assertFalse(form.is_valid())
