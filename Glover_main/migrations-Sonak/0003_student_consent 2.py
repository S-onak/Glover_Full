# Generated by Django 3.2.21 on 2023-09-28 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Glover_main', '0002_remove_student_consent'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='consent',
            field=models.BooleanField(default=False),
        ),
    ]