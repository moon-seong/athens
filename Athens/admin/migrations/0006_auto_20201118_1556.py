# Generated by Django 3.1.2 on 2020-11-18 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0005_auto_20201117_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consult_tbl',
            name='t_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin.teacher_tbl'),
        ),
    ]
