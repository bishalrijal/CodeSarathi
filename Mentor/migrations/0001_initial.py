# Generated by Django 2.0.5 on 2018-06-22 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photos', models.ImageField(blank=True, upload_to='mentor/%Y/%m/%d')),
                ('bio', models.CharField(blank=True, max_length=200, null=True)),
                ('rating', models.IntegerField(choices=[('1', 1), ('2', 2), ('3', 3)], null=True)),
                ('status', models.CharField(choices=[('available', 'Available'), ('unavailable', 'Unavailable')], default='unavailable', max_length=15)),
                ('github', models.URLField(null=True)),
            ],
        ),
    ]
