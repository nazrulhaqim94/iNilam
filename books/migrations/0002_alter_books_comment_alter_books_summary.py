# Generated by Django 4.0.2 on 2022-06-01 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='comment',
            field=models.TextField(default='Approved'),
        ),
        migrations.AlterField(
            model_name='books',
            name='summary',
            field=models.TextField(max_length=1000),
        ),
    ]
