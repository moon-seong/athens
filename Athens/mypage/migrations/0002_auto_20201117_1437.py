# Generated by Django 3.1.2 on 2020-11-17 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance_tbl',
            name='tr_no',
        ),
        migrations.RemoveField(
            model_name='consult_tbl',
            name='c_no',
        ),
        migrations.RemoveField(
            model_name='consult_tbl',
            name='t_no',
        ),
        migrations.DeleteModel(
            name='faq_tbl',
        ),
        migrations.RemoveField(
            model_name='lecture_tbl',
            name='t_no',
        ),
        migrations.DeleteModel(
            name='notice_tbl',
        ),
        migrations.RemoveField(
            model_name='online_tbl',
            name='l_no',
        ),
        migrations.RemoveField(
            model_name='test_tbl',
            name='tr_no',
        ),
        migrations.RemoveField(
            model_name='training_tbl',
            name='c_no',
        ),
        migrations.RemoveField(
            model_name='training_tbl',
            name='l_no',
        ),
        migrations.DeleteModel(
            name='attendance_tbl',
        ),
        migrations.DeleteModel(
            name='consult_tbl',
        ),
        migrations.DeleteModel(
            name='customer_tbl',
        ),
        migrations.DeleteModel(
            name='lecture_tbl',
        ),
        migrations.DeleteModel(
            name='online_tbl',
        ),
        migrations.DeleteModel(
            name='teacher_tbl',
        ),
        migrations.DeleteModel(
            name='test_tbl',
        ),
        migrations.DeleteModel(
            name='training_tbl',
        ),
    ]
