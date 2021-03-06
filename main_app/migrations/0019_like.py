# Generated by Django 3.1.2 on 2020-11-05 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0018_remove_profile_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.profile')),
                ('travelpost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.travelpost')),
            ],
        ),
    ]
