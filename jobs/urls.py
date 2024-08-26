# jobs/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add_job/', views.add_job, name='add_job'),
    path('', views.home, name='home'),  # Ensure the home view is mapped correctly
    path('edit_job/<int:job_id>/', views.edit_job, name='edit_job'),  # Assuming this is for future use
    path('delete_job/<int:job_id>/', views.delete_job, name='delete_job'),
]