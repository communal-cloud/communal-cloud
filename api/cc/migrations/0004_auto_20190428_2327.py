# Generated by Django 2.1.8 on 2019-04-28 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cc', '0003_auto_20190428_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='Categories',
            field=models.ManyToManyField(blank=True, related_name='Categories', to='cc.Category'),
        ),
    ]