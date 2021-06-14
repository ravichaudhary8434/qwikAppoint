# Generated by Django 3.2.4 on 2021-06-13 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='full_name',
            field=models.CharField(default='Name', max_length=70),
        ),
        migrations.AlterField(
            model_name='profile',
            name='type',
            field=models.CharField(choices=[('user', 'User'), ('org', 'Organization')], default='User', max_length=20),
        ),
    ]
