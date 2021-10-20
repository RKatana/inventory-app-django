from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.hashers import make_password


#Create your managers here
class UserManager(BaseUserManager):

    def create_user(self, email,password, **extra_fields):
        if not email:
            raise ValueError(_('User must set an email address'))
        if not password:
            raise ValueError(_('User must set a password'))
        email = self.normalize_email(email)

        user = self.model(
            email = email,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self,email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 'Merchant')

        if extra_fields.get('role') != 'Merchant':
            raise ValueError(_('Superuser must have role of Global Admin.'))
        return self.create_user(email, password, **extra_fields)


class StoreAdminManager(BaseUserManager):
    
    def create_user(self, email,password, **extra_fields):
        if not email:
            raise ValueError(_('User must set an email address'))
        if not password:
            raise ValueError(_('User must set a password'))
        email = self.normalize_email(email)

        storeadmin = self.model(
            email = email,
            **extra_fields
        )
        storeadmin.set_password(password)
        storeadmin.save()
        return storeadmin
