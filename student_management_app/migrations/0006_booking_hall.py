# Generated by Django 5.0.1 on 2024-07-12 18:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0005_remove_booking_hall_delete_college_delete_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking_hall',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('days', models.CharField(max_length=255)),
                ('timee', models.TimeField(max_length=255)),
                ('timeeend', models.TimeField(max_length=255)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student_management_app.courses')),
                ('hall_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_management_app.hall')),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_management_app.subjects')),
            ],
        ),
    ]
