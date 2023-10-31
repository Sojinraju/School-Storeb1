# Generated by Django 4.2.5 on 2023-09-12 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0005_alter_student_course_delete_course_delete_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='notebook',
        ),
        migrations.RemoveField(
            model_name='student',
            name='paper',
        ),
        migrations.RemoveField(
            model_name='student',
            name='pen',
        ),
        migrations.AddField(
            model_name='student',
            name='material',
            field=models.BooleanField(default=False),
        ),
    ]
