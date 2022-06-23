# Generated by Django 4.0.2 on 2022-06-02 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_alter_userprofile_darjah_alter_userprofile_kelas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(blank=True, choices=[('Teacher', 'Guru'), ('Student', 'Pelajar')], max_length=100, null=True),
        ),
    ]
