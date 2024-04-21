from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from users.models import CustomUser
from .serializers import CustomUserSerializer

@api_view(['POST'])
def signup(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        response_data = {
            'user_id': user.id,
            'message': 'User created successfully',
        }
        return Response(response_data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def log_in(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({
                'user_id': user.id,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'position': user.position,
                'phone_number': user.phone_number,
                'gender': user.gender,
                'profile_picture': user.profile_picture.url if user.profile_picture else None,
                'age': user.age
            })
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=400)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)

@api_view(['POST'])    
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'message': 'Logout successful'}, status=200)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)

@api_view(['GET'])
def get_user(request, user_id):
    try:
        user = CustomUser.objects.get(id=user_id)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except CustomUser.DoesNotExist:
        return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_user(request, user_id):
    try:
        user = CustomUser.objects.get(id=user_id)
        user.delete()
        return JsonResponse({'message': 'User deleted successfully'}, status=200)
    except CustomUser.DoesNotExist:
        return JsonResponse({'message': 'User not found'}, status=404)


@api_view(['PUT'])
def update_profile(request, user_id):
    try:
        profile = CustomUser.objects.get(id=user_id)
        serializer = CustomUserSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            # Check if 'profile_picture' is in request data
            if 'profile_picture' in request.FILES:
                # Delete the old profile picture if it exists
                if profile.profile_picture:
                    profile.profile_picture.delete()
                # Save the new profile picture
                profile.profile_picture = request.FILES['profile_picture']
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except CustomUser.DoesNotExist:
        return Response({'message': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)