from django.urls import path
from rest_framework.routers import DefaultRouter
from users.views import UsuarioViewSet
app_name = 'usuarios'

router = DefaultRouter()
router.register(r'usuario', UsuarioViewSet, basename="clientes")

urlpatterns = [
    
]+router.urls
