# Generated by Django 4.1 on 2022-09-23 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0003_profile_is_delete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_delete',
        ),
    ]
