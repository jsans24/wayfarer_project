# Generated by Django 3.1.2 on 2020-11-02 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_merge_20201102_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelpost',
            name='likes',
            field=models.IntegerField(),
        ),
    ]