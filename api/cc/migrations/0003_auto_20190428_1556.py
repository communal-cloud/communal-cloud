# Generated by Django 2.1.7 on 2019-04-28 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cc', '0002_activationtoken'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activationtoken',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='activationtoken',
            name='password',
        ),
    ]