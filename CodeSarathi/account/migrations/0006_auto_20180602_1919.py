# Generated by Django 2.0.5 on 2018-06-02 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20180601_2236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='techskill',
            name='languages',
        ),
        migrations.AddField(
            model_name='techskill',
            name='languages',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Languages'),
        ),
    ]