from users.models import User
from rest_framework import serializers

class CreateUserSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        return User.objects.create_user(
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            phone_number = validated_data['phone_number']
        )
    
    class Meta:
        model = User
        fields = '__all__'
    
