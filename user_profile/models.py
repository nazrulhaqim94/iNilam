from django.db import models
from accounts.models import User

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

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    role = models.CharField(choices=ROLE_CHOICES, blank=True, null=True, max_length=100)
    darjah = models.CharField(choices=DARJAH, blank=True, null=True, max_length=100)
    kelas = models.CharField(choices=KELAS, blank=True, null=True, max_length=100)

    def __str__(self):
        return self.first_name
