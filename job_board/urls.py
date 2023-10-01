from django.urls import path

from .views import index, job_detail

urlpatterns = [
    path('', index),
    path('job/<int:job_id>', job_detail, name='job-detail'),
]
