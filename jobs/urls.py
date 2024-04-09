from django.urls import path
from .views import add_job, delete_job, job_details, update_job

urlpatterns = [
    path('add/', add_job, name='add'),
    path('details/<int:user_id>/', job_details),
    path('update/<int:job_id>/', update_job),
    path('delete/<int:job_id>/', delete_job),
]
