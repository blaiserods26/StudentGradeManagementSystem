from django import forms
from accounts.models import User
from .models import Student

class StudentCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    current_class = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'identification_number')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def clean_identification_number(self):
        identification_number = self.cleaned_data.get('identification_number')
        if User.objects.filter(identification_number=identification_number).exists():
            raise forms.ValidationError("This ID number is already in use")
        return identification_number 


from django import forms
from accounts.models import User  # Import the User model
from .models import StudentMarks

class StudentMarksForm(forms.ModelForm):
    student_id = forms.ModelChoiceField(
        queryset=User.objects.filter(user_type=User.STUDENT),  # Filter for students
        empty_label="Select Student",  # Optionally add a placeholder
        to_field_name="identification_number",  # Display the 'identification_number' field of the User
        widget=forms.Select(attrs={'class': 'form-control'})  # Optional styling
    )

    class Meta:
        model = StudentMarks
        fields = ['student_id', 'java', 'python', 'dbms', 'data_science', 'aoa', 'iks']
