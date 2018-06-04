# Generated by Django 2.0.5 on 2018-05-31 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_profile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TechSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(blank=True, max_length=2000, null=True)),
                ('languages', models.ManyToManyField(to='account.Languages')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='skill',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.TechSkill'),
        ),
    ]
