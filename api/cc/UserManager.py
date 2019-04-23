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
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user