from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CustomUserSerializer

@api_view(['POST'])
def signup(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .serializers import UserSerializer

# @api_view(['POST'])
# def signup(request):
#     if request.method == 'POST':
#         first_name = request.data.get('first_name')
#         last_name = request.data.get('last_name')
#         email = request.data.get('email')
#         password = request.data.get('password')

#         if not all([first_name, last_name, email, password]):
#             return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)

#         serializer = UserSerializer(data={'first_name': first_name, 'last_name': last_name, 'email': email, 'password': password})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
