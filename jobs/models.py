from django.db import models
from users.models import CustomUser

class Jobs(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    job_name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    duration = models.CharField(max_length=10, choices=[('part-time', 'Part-time'), ('full-time', 'Full-time')], blank=True)
    description = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='profile_pictures/', blank=True)
    salary = models.IntegerField(blank=True, null=True)