# Generated by Django 4.1 on 2022-09-18 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='use',
            new_name='user',
        ),
    ]
