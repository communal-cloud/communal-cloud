from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    
    use_in_migrations = True

    def create_user(self, username, email, name, password):
        user = self.model(
            username = username,
            email = self.normalize_email(email),
            name = name,
        )
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_staffuser(self, username, email, name, password):
        user = self.create_user(
            username = username,
            email = email,
            name = name,
            password = password,
        )
        user.staff = True
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, name, password):
        user = self.create_user(
            username = username,
            email = email,
            name = name,
            password = password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user