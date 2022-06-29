# Generated by Django 4.0.2 on 2022-05-29 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='kelas',
            field=models.CharField(blank=True, choices=[('Intan', 'Intan'), ('Nilam', 'Nilam')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('Teacher', 'Teacher'), ('Student', 'Student')], max_length=100, null=True),
        ),
    ]
