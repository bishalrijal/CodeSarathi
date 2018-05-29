# Generated by Django 2.0.5 on 2018-05-29 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('photos', models.ImageField(blank=True, upload_to='users/%Y/%m/%d')),
                ('bio', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
