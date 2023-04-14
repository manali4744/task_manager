# Generated by Django 3.2.18 on 2023-04-14 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_auto_20230414_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='submitted_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='task_has_reportee',
            name='Priority',
            field=models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], default='Medium', max_length=250),
        ),
    ]