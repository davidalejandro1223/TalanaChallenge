from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, VerifyUserView
app_name = 'usuarios'

router = DefaultRouter()
router.register(r'usuario', UsuarioViewSet, basename="clientes")

urlpatterns = [
    path('account/verify/<str:token>', VerifyUserView.as_view(), name='verify_account')
]+router.urls
