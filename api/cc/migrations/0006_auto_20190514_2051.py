# Generated by Django 2.1.7 on 2019-05-14 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cc', '0005_workflow_community_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cc.BaseModel')),
                ('Banned', models.BooleanField(default=False)),
                ('Community', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cc.Community')),
                ('Roles', models.ManyToManyField(blank=True, to='cc.Role')),
            ],
            bases=('cc.basemodel',),
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AddField(
            model_name='member',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]