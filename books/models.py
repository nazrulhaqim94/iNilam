from django.db import models
import uuid
from accounts.models import User
import datetime

# Create your models here.

BM = 1
ENG = 2

LANGUAGE = (
  (BM, 'Bahasa Malaysia'),
  (ENG, 'English')
)

FIC = 1
NFIC = 2

TAGS = (
  (FIC, 'Fiction'),
  (NFIC, 'Non - Fiction')
)

class Books(models.Model):
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4, verbose_name='Public identifier')
    book_title = models.CharField(max_length=100)
    book_author = models.CharField(max_length=100)
    date_published = models.DateField(null=True)
    date_read = models.DateField(null=True)
    page = models.IntegerField(default=1)
    language = models.PositiveSmallIntegerField(choices=LANGUAGE, null=True)
    tags = models.PositiveSmallIntegerField(choices=TAGS, null=True)
    summary = models.TextField(max_length=1000)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    approval_status = models.CharField(max_length=100)
    comment = models.TextField(default="Approved")

    def __str__(self):
        return self.book_title