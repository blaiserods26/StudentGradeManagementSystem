from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def dashboard(request):
    return render(request, 'management/dashboard.html')

@login_required
def create_student(request):
    if request.method == 'POST':
        # Add student creation logic here
        pass
    return render(request, 'management/create_student.html')

@login_required
def add_marks(request):
    if request.method == 'POST':
        # Add marks submission logic here
        pass
    return render(request, 'management/add_marks.html')

@login_required
def view_students(request):
    # Add logic to fetch students here
    students = []  # Replace with actual student query
    return render(request, 'management/view_students.html', {'students': students})
