# Generated by Django 3.2.18 on 2023-04-11 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0003_auto_20230411_0932'),
        ('task', '0013_auto_20230411_1018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task_Has_Reportee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='project_has_reporter',
            name='Project_Name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.project'),
        ),
        migrations.DeleteModel(
            name='Project_has_Task',
        ),
        migrations.AddField(
            model_name='task_has_reportee',
            name='Project_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.project_has_reporter'),
        ),
        migrations.AddField(
            model_name='task_has_reportee',
            name='Reportee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_app.reportee'),
        ),
        migrations.AddField(
            model_name='task_has_reportee',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.task'),
        ),
    ]
