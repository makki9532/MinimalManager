# Generated by Django 4.1 on 2023-04-28 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_user_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='type',
        ),
        migrations.AddField(
            model_name='taskplanner',
            name='is_completed',
            field=models.BooleanField(null=True),
        ),
    ]
