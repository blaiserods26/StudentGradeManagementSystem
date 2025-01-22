from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import StudentCreationForm
from accounts.models import User
from .models import Student

def is_management_user(user):
    return user.is_authenticated and user.user_type == User.MANAGEMENT

@login_required
@user_passes_test(is_management_user)
def create_student(request):
    if request.method == 'POST':
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            # Create user account
            user = form.save(commit=False)
            user.username = form.cleaned_data['identification_number']
            user.user_type = User.STUDENT
            user.set_password(form.cleaned_data['password1'])
            user.save()

            # Create student profile
            Student.objects.create(
                user=user,
                date_of_birth=form.cleaned_data['date_of_birth'],
                current_class=form.cleaned_data['current_class']
            )

            messages.success(request, f'Student account created successfully for {user.get_full_name()}')
            return redirect('management:view_students')
        else:
            messages.error(request, 'Error creating student account. Please check the form.')
    else:
        form = StudentCreationForm()
    
    return render(request, 'management/create_student.html', {'form': form})

@login_required
@user_passes_test(is_management_user)
def dashboard(request):
    return render(request, 'management/dashboard.html')

@login_required
@user_passes_test(is_management_user)
def add_marks(request):
    return render(request, 'management/add_marks.html')

@login_required
@user_passes_test(is_management_user)
def view_students(request):
    students = Student.objects.all()
    return render(request, 'management/view_students.html', {'students': students})
