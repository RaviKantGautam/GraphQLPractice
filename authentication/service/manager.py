from django.contrib.auth.models import BaseUserManager


# -------------------------------------------------------------------------------
# ManagerAccountUser
# -------------------------------------------------------------------------------
class ManagerAccountUser(BaseUserManager):
    """
    Provides manager methods for the user model.
    """

    # ---------------------------------------------------------------------------
    # create_user
    # ---------------------------------------------------------------------------
    def create_user(self, username=None, email=None, **kwargs):
        """
        This method creates a new user and its associated profile(empty)
        that can be updated whenever required.
        """
        if username is None:
            raise ValueError('Users must have a username.')
        
        try:
            password = kwargs.pop('password')

        except KeyError:
            password = ''

        if email is not None:
            user = self.model(email=self.normalize_email(email), is_verified=True, **kwargs)
        else:
            user = self.model(is_verified=True, **kwargs)
        
        user.username = str(username).replace(' ', '_')

       # update user password

        user.set_password(password)

        # save the new user
        user.save(using=self._db)
        
        return user

    # ---------------------------------------------------------------------------
    # create_superuser
    # ---------------------------------------------------------------------------
    def create_superuser(self, username, password):
        """
        This method creates a superuser for the system.
        
        It takes following arguments:
        1) email - email of superuser (required)
        2) password - strong password of superuser (required)
        3) is_active - set to true
        """

        user = self.create_user(username=str(username).replace(" ", "_"),
                                password=password,
                                is_staff=True,
                                is_superuser=True,
                                is_active=True
                                )

        return user
