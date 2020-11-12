from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

# Users
from users.models import User
from users.serializers import CreateUserSerializer
# Create your views here.

class UsuarioViewSet(ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateUserSerializer