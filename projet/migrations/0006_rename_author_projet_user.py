# Generated by Django 4.1 on 2022-09-22 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projet', '0005_alter_projet_categori_alter_projet_foto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projet',
            old_name='author',
            new_name='user',
        ),
    ]
