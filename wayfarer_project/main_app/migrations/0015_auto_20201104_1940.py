# Generated by Django 3.1.3 on 2020-11-04 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_auto_20201104_1836'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_pic',
            new_name='image',
        ),
    ]