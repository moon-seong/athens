# Generated by Django 3.1.2 on 2020-11-17 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher_tbl',
            name='t_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
