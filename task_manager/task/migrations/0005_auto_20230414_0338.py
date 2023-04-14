# Generated by Django 3.2.18 on 2023-04-14 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_auto_20230413_0949'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task_has_reportee',
            options={'ordering': ['Priority']},
        ),
        migrations.AddField(
            model_name='task_has_reportee',
            name='Priority',
            field=models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], default='Low', max_length=250),
        ),
    ]
