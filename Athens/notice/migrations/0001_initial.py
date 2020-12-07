# Generated by Django 3.1.3 on 2020-11-11 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer_tbl',
            fields=[
                ('c_no', models.AutoField(primary_key=True, serialize=False)),
                ('c_name', models.CharField(max_length=10)),
                ('c_id', models.CharField(max_length=40, unique=True)),
                ('c_pw', models.CharField(max_length=100)),
                ('c_phone', models.CharField(max_length=20)),
                ('c_gender', models.CharField(choices=[('남성', '남성'), ('여성', '여성')], max_length=10)),
                ('c_join', models.DateField(auto_now_add=True)),
                ('c_birth', models.DateField()),
                ('c_code', models.CharField(blank=True, max_length=6, null=True)),
                ('c_add', models.CharField(blank=True, max_length=50, null=True)),
                ('c_school', models.CharField(blank=True, max_length=50, null=True)),
                ('c_state', models.BooleanField()),
                ('c_out', models.DateField(null=True)),
                ('c_code_valid', models.CharField(max_length=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='faq_tbl',
            fields=[
                ('faq_no', models.AutoField(primary_key=True, serialize=False)),
                ('faq_question', models.TextField()),
                ('faq_answer', models.TextField()),
                ('faq_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='lecture_tbl',
            fields=[
                ('l_no', models.AutoField(primary_key=True, serialize=False)),
                ('l_totalnum', models.IntegerField()),
                ('l_term', models.IntegerField()),
                ('l_pay', models.IntegerField()),
                ('l_startdate', models.DateField()),
                ('l_desc', models.CharField(max_length=200, null=True)),
                ('l_img', models.ImageField(blank=True, upload_to='lecture')),
                ('l_dept', models.CharField(max_length=10)),
                ('l_class', models.IntegerField()),
                ('l_subject', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='notice_tbl',
            fields=[
                ('notice_no', models.AutoField(primary_key=True, serialize=False)),
                ('notice_title', models.CharField(max_length=200)),
                ('n_writer', models.CharField(max_length=20)),
                ('notice_date', models.DateTimeField()),
                ('notice_target', models.CharField(max_length=20)),
                ('notice_content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='teacher_tbl',
            fields=[
                ('t_no', models.AutoField(primary_key=True, serialize=False)),
                ('t_name', models.CharField(max_length=10)),
                ('t_id', models.CharField(max_length=40, unique=True)),
                ('t_pw', models.CharField(max_length=100)),
                ('t_phone', models.CharField(max_length=20, null=True)),
                ('t_gender', models.CharField(choices=[('남성', '남성'), ('여성', '여성')], max_length=10)),
                ('t_birth', models.DateField()),
                ('t_state', models.BooleanField()),
                ('t_add', models.CharField(max_length=50, null=True)),
                ('t_join', models.DateField(auto_now_add=True)),
                ('t_file', models.ImageField(blank=True, null=True, upload_to='teacher/')),
                ('t_out', models.DateField(null=True)),
                ('t_text', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='training_tbl',
            fields=[
                ('tr_no', models.AutoField(primary_key=True, serialize=False)),
                ('tr_date', models.DateField(auto_now_add=True)),
                ('c_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notice.customer_tbl')),
                ('l_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notice.lecture_tbl')),
            ],
        ),
        migrations.CreateModel(
            name='test_tbl',
            fields=[
                ('te_no', models.AutoField(primary_key=True, serialize=False)),
                ('te_name', models.CharField(max_length=200)),
                ('te_score', models.IntegerField(blank=True, null=True)),
                ('te_date', models.DateField()),
                ('tr_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notice.training_tbl')),
            ],
        ),
        migrations.CreateModel(
            name='online_tbl',
            fields=[
                ('on_no', models.AutoField(primary_key=True, serialize=False)),
                ('on_title', models.CharField(max_length=200)),
                ('on_content', models.TextField()),
                ('on_date', models.DateTimeField()),
                ('on_div', models.CharField(max_length=20)),
                ('on_file', models.FileField(blank=True, upload_to='online/')),
                ('l_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notice.lecture_tbl')),
            ],
        ),
        migrations.AddField(
            model_name='lecture_tbl',
            name='t_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notice.teacher_tbl'),
        ),
        migrations.CreateModel(
            name='consult_tbl',
            fields=[
                ('cu_no', models.AutoField(primary_key=True, serialize=False)),
                ('cu_cust', models.CharField(max_length=20)),
                ('cu_join_time', models.DateTimeField()),
                ('cu_res_time', models.DateTimeField()),
                ('cu_content', models.TextField(blank=True, null=True)),
                ('cu_state', models.CharField(blank=True, max_length=10, null=True)),
                ('c_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notice.customer_tbl')),
                ('t_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notice.training_tbl')),
            ],
        ),
        migrations.CreateModel(
            name='attendance_tbl',
            fields=[
                ('at_no', models.AutoField(primary_key=True, serialize=False)),
                ('attendance', models.CharField(max_length=20)),
                ('at_date', models.DateField()),
                ('tr_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notice.training_tbl')),
            ],
        ),
    ]