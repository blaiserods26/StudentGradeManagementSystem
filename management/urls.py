from django.urls import path
from . import views

app_name = 'management'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-student/', views.create_student, name='create_student'),
    path('add-marks/', views.add_marks, name='add_marks'),
    path('view-students/', views.view_students, name='view_students'),
] 