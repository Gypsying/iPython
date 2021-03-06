# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-19 15:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='跟进日期')),
                ('note', models.TextField(verbose_name='跟进内容...')),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.UserInfo', verbose_name='跟踪人')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Customer', verbose_name='所咨询客户')),
            ],
        ),
        migrations.CreateModel(
            name='CourseRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_num', models.IntegerField(help_text='此处填写第几节课或第几天课程...,必须为数字', verbose_name='节次')),
                ('date', models.DateField(auto_now_add=True, verbose_name='上课日期')),
                ('course_title', models.CharField(blank=True, max_length=64, null=True, verbose_name='本节课程标题')),
                ('course_memo', models.TextField(blank=True, null=True, verbose_name='本节课程内容概要')),
                ('has_homework', models.BooleanField(default=True, verbose_name='本节有作业')),
                ('homework_title', models.CharField(blank=True, max_length=64, null=True, verbose_name='本节作业标题')),
                ('homework_memo', models.TextField(blank=True, max_length=500, null=True, verbose_name='作业描述')),
                ('exam', models.TextField(blank=True, max_length=300, null=True, verbose_name='踩分点')),
                ('class_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.ClassList', verbose_name='班级')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.UserInfo', verbose_name='讲师')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_type', models.IntegerField(choices=[(1, '订金/报名费'), (2, '学费'), (3, '转班'), (4, '退学'), (5, '退款')], default=1, verbose_name='费用类型')),
                ('paid_fee', models.IntegerField(default=0, verbose_name='费用数额')),
                ('turnover', models.IntegerField(blank=True, null=True, verbose_name='成交金额')),
                ('quote', models.IntegerField(blank=True, null=True, verbose_name='报价金额')),
                ('note', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='交款日期')),
                ('class_list', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.ClassList', verbose_name='班级')),
                ('consultant', models.ForeignKey(help_text='谁签的单就选谁', on_delete=django.db.models.deletion.CASCADE, to='crm.UserInfo', verbose_name='负责老师')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Customer', verbose_name='客户')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('emergency_contract', models.CharField(blank=True, max_length=32, null=True, verbose_name='紧急联系人')),
                ('company', models.CharField(blank=True, max_length=128, null=True, verbose_name='公司')),
                ('location', models.CharField(blank=True, max_length=64, null=True, verbose_name='所在区域')),
                ('position', models.CharField(blank=True, max_length=64, null=True, verbose_name='岗位')),
                ('salary', models.IntegerField(blank=True, null=True, verbose_name='薪资')),
                ('welfare', models.CharField(blank=True, max_length=256, null=True, verbose_name='福利')),
                ('date', models.DateField(blank=True, help_text='格式yyyy-mm-dd', null=True, verbose_name='入职时间')),
                ('memo', models.CharField(blank=True, max_length=256, null=True, verbose_name='备注')),
                ('class_list', models.ManyToManyField(blank=True, to='crm.ClassList', verbose_name='已报班级')),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='crm.Customer', verbose_name='客户信息')),
            ],
        ),
        migrations.CreateModel(
            name='StudyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record', models.CharField(choices=[('checked', '已签到'), ('vacate', '请假'), ('late', '迟到'), ('noshow', '缺勤'), ('leave_early', '早退')], default='checked', max_length=64, verbose_name='上课纪录')),
                ('score', models.IntegerField(choices=[(100, 'A+'), (90, 'A'), (85, 'B+'), (80, 'B'), (70, 'B-'), (60, 'C+'), (50, 'C'), (40, 'C-'), (0, ' D'), (-1, 'N/A'), (-100, 'COPY'), (-1000, 'FAIL')], default=-1, verbose_name='本节成绩')),
                ('homework_note', models.CharField(blank=True, max_length=255, null=True, verbose_name='作业评语')),
                ('note', models.CharField(blank=True, max_length=255, null=True, verbose_name='备注')),
                ('homework', models.FileField(blank=True, default=None, null=True, upload_to='', verbose_name='作业文件')),
                ('stu_memo', models.TextField(blank=True, null=True, verbose_name='学员备注')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='提交作业日期')),
                ('course_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.CourseRecord', verbose_name='第几天课程')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Student', verbose_name='学员')),
            ],
        ),
    ]
