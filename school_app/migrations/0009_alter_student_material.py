# Generated by Django 4.2.5 on 2023-09-13 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0008_alter_student_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='material',
            field=models.BooleanField(choices=[('Note', 'Note'), ('pen', 'pen'), ('paper', 'paper')], default=False),
        ),
    ]