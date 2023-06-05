# Generated by Django 4.1 on 2023-04-28 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_project_project_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('S', 'Student'), ('E', 'Educator'), ('A', 'Admin')], max_length=1, null=True),
        ),
    ]