# Generated by Django 5.0.1 on 2024-07-11 01:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('capacity', models.IntegerField()),
                ('projector_available', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='schedules_m',
            name='hall_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='student_management_app.hall'),
            preserve_default=False,
        ),
    ]
