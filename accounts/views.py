from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required
from .forms import CustomAuthenticationForm, ManagementSignUpForm

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            identification_number = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=identification_number, password=password)
            if user is not None:
                login(request, user)
                if user.is_staff:
                    return redirect('management:dashboard')
                else:
                    return redirect('accounts:student_dashboard')
            else:
                messages.error(request, 'Invalid identification number or password.')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('accounts:login')

def management_signup_view(request):
    if request.method == 'POST':
        form = ManagementSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully. Please login.')
            return redirect('accounts:login')
        else:
            messages.error(request, 'Error creating account. Please check the form.')
    else:
        form = ManagementSignUpForm()
    return render(request, 'accounts/management_signup.html', {'form': form})

@login_required
def student_dashboard(request):
    student_info = {}  # Replace with actual student data query
    return render(request, 'accounts/student_dashboard.html', {'student_info': student_info})

@login_required
def view_marks(request):
    # Add logic to fetch student's marks
    student_marks = {}  # Replace with actual marks query
    return render(request, 'accounts/view_marks.html', {'marks': student_marks})

@login_required
def profile(request):
    # Get the current user's profile information
    user = request.user
    context = {
        'user': user,
        # Add any additional profile information you want to display
    }
    return render(request, 'accounts/profile.html', context) 