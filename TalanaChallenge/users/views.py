#Django
from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import FormView
from django.http.response import HttpResponse

# Utilities
import jwt

from rest_framework.viewsets import ModelViewSet

# Users
from .models import User
from .serializers import CreateUserSerializer

# forms
from .forms import SetPasswordForm
# Create your views here.

class UsuarioViewSet(ModelViewSet):
    queryset = User.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateUserSerializer
    
class VerifyUserView(FormView):
    template_name = 'users/set_user_password.html'
    form_class = SetPasswordForm
    success_url = '/account_verified/'

    def form_valid(self, form) -> HttpResponse:
        token = jwt.decode(self.kwargs['token'], settings.SECRET_KEY, algorithms='HS256')
        user = get_object_or_404(User, email=token['user'])
        user.set_password(form.cleaned_data['password'])
        user.is_active = True
        user.save()
        return HttpResponse('Tu cuenta ha sido activada')
