from statistics import mode
import uuid
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone


from .managers import CustomUserManager

STUDENT = "Student"
TEACHER = "Teacher"

ROLE_CHOICES = (
        (TEACHER, 'Guru'),
        (STUDENT, 'Pelajar')
    )

DARJAH1 = "1"
DARJAH2 = "2"

DARJAH = (
  (DARJAH1, 'Darjah 1'),
  (DARJAH2, 'Darjah 2')
)

KELAS1 = "Intan"
KELAS2 = "Nilam"

KELAS = (
  (KELAS1, 'Intan'),
  (KELAS2, 'Nilam')
)


class User(AbstractBaseUser, PermissionsMixin):

  # Roles created here
  uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4, verbose_name='Public identifier')
  email = models.EmailField(unique=True)
  first_name = models.CharField(max_length=30, blank=True)
  last_name = models.CharField(max_length=50, blank=True)
  role = models.CharField(choices=ROLE_CHOICES, blank=True, null=True, max_length=100)
  darjah = models.CharField(choices=DARJAH, blank=True, null=True, max_length=100)
  kelas = models.CharField(choices=KELAS, blank=True, null=True, max_length=100)
  date_joined = models.DateTimeField(auto_now_add=True)
  is_active = models.BooleanField(default=True)
  is_deleted = models.BooleanField(default=False)
  created_date = models.DateTimeField(default=timezone.now)
  modified_date = models.DateTimeField(default=timezone.now)
  created_by = models.EmailField()
  modified_by = models.EmailField()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  objects = CustomUserManager()

  class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

  def __str__(self):
    return self.email