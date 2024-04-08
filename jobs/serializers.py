from .models import Jobs
from rest_framework import serializers


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = ['id', 'user', 'job_name', 'country', 'city', 'duration', 'description', 'logo', 'salary']
