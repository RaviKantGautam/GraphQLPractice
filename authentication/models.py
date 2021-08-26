from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from graphql_django.db import *
from .service import *

# Create your models here.

# class User(AbstractBaseUser, ModelAbstractBase, PermissionsMixin):
#     """
#     Create Users with role
#     """
#     email = models.EmailField(help_text='Email of user', unique=True)
#     username = models.CharField(max_length=50, help_text="Enter your username.", unique=True)
#     first_name = models.CharField(max_length=20, blank=True, default='', null=True,
#                                   help_text='First Name of user', )
#     last_name = models.CharField(max_length=20, blank=True, default='', null=True,
#                                  help_text='Name Name of user',)
#     is_active = models.BooleanField(default=True,
#                             help_text="Toggles active status for a user.")
#     is_staff = models.BooleanField(default=False,
#                                    help_text="Designates the user as "
#                                              "a staff member.")

#     is_superuser = models.BooleanField(default=False,
#                                        help_text="Designates the user as"
#                                                  " a super user.")
#     is_verified = models.BooleanField(default=False,
#                                       help_text="Toggles verification status for a user.")

#     objects = ManagerAccountUser()
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#     # -------------------------------------------------------------------------
#     # Meta
#     # -------------------------------------------------------------------------
#     class Meta:
#         db_table = "user"
#         verbose_name = "User"
#         verbose_name_plural = "Users"
#         indexes = [
#             models.Index(fields=['email',]),
#             models.Index(fields=['is_active',]),
#             models.Index(fields=['is_staff',]),
#             models.Index(fields=['is_verified',]),
#         ]

#     def __str__(self):
#         """
#         Returns the string representation of the user object.
#         """
#         return "@"+str(self.username)
    
#     def has_perm(self, perm, obj=None):
#         "Does the user have a specific permission?"
#         # Simplest possible answer: Yes, always
#         # print('perm: ',perm)
#         # return perm == 'Shopping.view'
#         return True

#     def has_module_perms(self, app_label):
#         "Does the user have permissions to view the app `app_label`?"
#         # Simplest possible answer: Yes, always
#         # if self.is_admin:
#         #     return True
#         # else:
#         #     return app_label=='Shopping'
#         return True
   

