from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/management/', views.management_signup_view, name='management_signup'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('student/marks/', views.view_marks, name='view_marks'),
    path('student/profile/', views.profile, name='profile'),
] 