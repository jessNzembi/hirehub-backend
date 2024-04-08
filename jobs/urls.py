from django.urls import path
from .views import add_job, job_details

urlpatterns = [
    path('add/', add_job, name='add'),
    path('details/<int:user_id>/', job_details, name='details'),
]
