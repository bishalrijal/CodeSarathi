# Generated by Django 2.0.5 on 2018-06-02 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0025_profile_follows'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='follows',
        ),
    ]
