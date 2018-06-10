# Generated by Django 2.0.5 on 2018-05-30 14:42

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0013_posts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Posts',
            new_name='Post',
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-created',)},
        ),
    ]