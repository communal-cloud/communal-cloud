from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    
    use_in_migrations = True

    def create_user(self, email, name, password):
        user = self.model(
            email = self.normalize_email(email),
            name = name,
        )
        user.set_password(password)
        user.is_superuser = False
        user.staff = False
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, name, password):
        user = self.create_user(
            email = email,
            name = name,
            password = password,
        )
        user.is_superuser = False
        user.staff = True
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(
            email = email,
            name = name,
            password = password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user