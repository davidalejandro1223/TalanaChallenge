"""Celery tasks."""

# Django
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone
from django.urls import reverse_lazy
# Models
from users.models import User

# Celery
from celery.decorators import task

# Utilities
import jwt
from datetime import timedelta


def gen_verification_token(user):
    """Crea JWT usado por el usuario para verificar su cuenta"""
    exp_date = timezone.now() + timedelta(days=3)
    payload = {
        'user': user.email,
        'exp': int(exp_date.timestamp()),
        'type': 'email_confirmation'
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token.decode()


@task(name='send_confirmation_email', max_retries=3)
def send_confirmation_email(user_pk):
    """Envia correo de verificacion al usuario en cuestion"""
    print('enviando..')
    
    user = User.objects.get(pk=user_pk)
    verification_token = gen_verification_token(user)
    subject = 'Bienvenido {}! Verifica tu cuenta para participar en el sorteo'.format(user.first_name)
    from_email = 'Sorteo papel de por vida! <noreply@sorteopapel.com>'
    verification_url = reverse_lazy('users:verify_account', kwargs={'token':verification_token})
    
    content = render_to_string(
        'emails/users/account_verification.html',
        {'verification_url': verification_url, 'user': user}
    )
    print(content)
    
    msg = EmailMultiAlternatives(subject, content, from_email, [user.email])
    msg.content_subtype = 'html'
    msg.attach_alternative(content, "text/html")
    msg.send()
