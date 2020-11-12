from django.contrib.auth.models import UserManager
 
class UserManager (UserManager):
    """Manager para controlar la creacion de usuario y
    gestion de contraseñas"""

    def create_user(self, email, first_name, last_name, phone_number,**extra_fields):
        
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            is_active=False
        )

        user.save(using=self._db)
        return user

