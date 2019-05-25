# Generated by Django 2.1.8 on 2019-05-25 18:14

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cc', '0007_auto_20190525_1534'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workflow',
            old_name='Community_id',
            new_name='Community',
        ),
        migrations.AddField(
            model_name='datafield',
            name='Parameters',
            field=jsonfield.fields.JSONField(default='{}'),
        ),
        migrations.AddField(
            model_name='task',
            name='Type',
            field=models.IntegerField(choices=[(0, 'NotSpecified'), (1, 'Execution'), (2, 'Join'), (3, 'Leave')], default=0),
            preserve_default=False,
        ),
    ]