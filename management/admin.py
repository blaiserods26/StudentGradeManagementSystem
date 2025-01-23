from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from accounts.models import User
from .models import Student, StudentMarks

class CustomUserAdmin(UserAdmin):
    list_display = ('identification_number', 'first_name', 'last_name', 'email', 'user_type', 'is_active')
    list_filter = ('user_type', 'is_active', 'is_staff')
    search_fields = ('identification_number', 'first_name', 'last_name', 'email')
    ordering = ('identification_number',)
    
    fieldsets = (
        (None, {'fields': ('identification_number', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'user_type'),
        }),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('identification_number', 'email', 'first_name', 'last_name', 
                      'password1', 'password2', 'user_type', 'is_staff'),
        }),
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        
        if not is_superuser:
            if 'is_superuser' in form.base_fields:
                form.base_fields['is_superuser'].disabled = True
            if 'user_permissions' in form.base_fields:
                form.base_fields['user_permissions'].disabled = True
            if 'groups' in form.base_fields:
                form.base_fields['groups'].disabled = True
        
        return form

    def save_model(self, request, obj, form, change):
        if not change:  # If this is a new user
            # Set username to identification_number if not set
            if not obj.username:
                obj.username = obj.identification_number
                
            # Automatically set is_staff for management users
            if obj.user_type == User.MANAGEMENT:
                obj.is_staff = True
            else:
                obj.is_staff = False
                
        super().save_model(request, obj, form, change)

# Registering the Custom User Admin
admin.site.register(User, CustomUserAdmin)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'current_class', 'date_of_birth', 'created_at')
    search_fields = ('user__first_name', 'user__last_name', 'user__identification_number')
    list_filter = ('current_class',)

    def get_full_name(self, obj):
        return obj.user.get_full_name()
    get_full_name.short_description = 'Student Name'

# StudentMarks doesn't need a custom admin class unless you want to modify its display
admin.site.register(StudentMarks)
