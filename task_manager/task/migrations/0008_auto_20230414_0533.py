# Generated by Django 3.2.18 on 2023-04-14 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_alter_task_submitted_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='task_has_reportee',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='task_has_reportee',
            name='days',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='task_has_reportee',
            name='submitted_at',
            field=models.DateTimeField(null=True),
        ),
    ]