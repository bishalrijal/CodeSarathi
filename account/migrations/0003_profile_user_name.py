# Generated by Django 2.0.5 on 2018-05-27 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_profile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_name',
            field=models.CharField(default='.', max_length=100),
        ),
    ]