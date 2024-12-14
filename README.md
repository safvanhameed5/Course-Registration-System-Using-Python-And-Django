# Course Registration System

## Project Description
This Django project provides a simple Course Registration System. It allows students to view available courses, register for courses, and prevents registration if a course has reached its maximum capacity. The system consists of models for `Course` and `Student`, views for listing courses and handling registration, and responsive templates for the user interface.

## Features
- **Course Model**: Stores details about courses, including title, description, maximum capacity, and current enrollment.
- **Student Model**: Stores details about students, including their name, email, and the courses they are enrolled in.
- **Course Listing**: Displays all available courses.
- **Course Registration**: Allows students to register for courses, while ensuring a course's capacity is not exceeded.
- **Basic Validation**: Includes validation for course registration to ensure students cannot register for a full course.

