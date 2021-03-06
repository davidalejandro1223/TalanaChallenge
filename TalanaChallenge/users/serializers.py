#Django rest
from rest_framework import serializers

# Models
from .models import User

# Task
from .tasks import send_confirmation_email
class CreateUserSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            phone_number = validated_data['phone_number']
        )
        send_confirmation_email.delay(user_pk=user.pk)
        return user
    
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password':{
                'write_only':True
            }
        }
