from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(email=validated_data['email'], 
                                              first_name=validated_data['first_name'], 
                                              last_name=validated_data['last_name'],
                                              password=validated_data['password']
                                            )
        return user