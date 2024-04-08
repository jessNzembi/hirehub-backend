from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Jobs
from .serializers import JobSerializer

@api_view(['GET'])
def job_details(request, user_id):
    try:
        job = Jobs.objects.get(user_id=user_id)
        serializer = JobSerializer(job)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Jobs.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_job(request):
    if request.method == 'POST':
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
