# Generated by Django 3.1.3 on 2020-12-01 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0016_auto_20201201_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher_tbl',
            name='t_join',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
