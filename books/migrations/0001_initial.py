# Generated by Django 4.0.2 on 2022-05-20 17:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='Public identifier')),
                ('book_title', models.CharField(max_length=100)),
                ('book_author', models.CharField(max_length=100)),
                ('date_published', models.DateField(null=True)),
                ('date_read', models.DateField(null=True)),
                ('page', models.IntegerField(default=1)),
                ('language', models.PositiveSmallIntegerField(choices=[(1, 'Bahasa Malaysia'), (2, 'English')], null=True)),
                ('tags', models.PositiveSmallIntegerField(choices=[(1, 'Fiction'), (2, 'Non - Fiction')], null=True)),
                ('summary', models.TextField(default='TEST DATA')),
                ('approval_status', models.CharField(max_length=100)),
                ('comment', models.TextField()),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
