# Generated by Django 2.0.5 on 2018-05-30 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_auto_20180530_1809'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='created_by',
        ),
    ]
