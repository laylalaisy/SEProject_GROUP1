# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='account',
            fields=[
                ('account_id', models.CharField(primary_key=True, max_length=20, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('salt', models.CharField(max_length=8, default='12345678')),
                ('type', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='admin',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='apply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('note', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='assist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='belong',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='college',
            fields=[
                ('college_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('intro', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='course',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('credit', models.DecimalField(max_digits=3, decimal_places=1)),
                ('capacity', models.IntegerField()),
                ('intro', models.TextField()),
                ('type', models.CharField(max_length=40)),
                ('semester', models.CharField(max_length=10, default='Spring')),
            ],
        ),
        migrations.CreateModel(
            name='discipline',
            fields=[
                ('discipline_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('intro', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='evaluate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('point', models.DecimalField(max_digits=3, decimal_places=2)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='examination',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('position', models.IntegerField(null=True)),
                ('date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='learn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('grade', models.IntegerField(null=True)),
                ('status', models.IntegerField(default=0)),
                ('course_id', models.ForeignKey(to='basicInfo.course')),
            ],
        ),
        migrations.CreateModel(
            name='log',
            fields=[
                ('log_id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='major',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('studnet_id', models.IntegerField()),
                ('discipline_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='master',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('college_id', models.ForeignKey(to='basicInfo.college')),
            ],
        ),
        migrations.CreateModel(
            name='minor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('studnet_id', models.IntegerField()),
                ('discipline_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='operation',
            fields=[
                ('operation_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='pre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('tmp_course_id', models.IntegerField()),
                ('pre_course_id', models.ForeignKey(to='basicInfo.course')),
            ],
        ),
        migrations.CreateModel(
            name='quit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('note', models.TextField()),
                ('course_id', models.ForeignKey(to='basicInfo.course')),
            ],
        ),
        migrations.CreateModel(
            name='room',
            fields=[
                ('room_id', models.AutoField(primary_key=True, serialize=False)),
                ('capacity', models.IntegerField()),
                ('location', models.CharField(max_length=40)),
                ('type', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('student_id', models.CharField(primary_key=True, max_length=20, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('dorm', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='suspend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('course_id', models.ForeignKey(to='basicInfo.course')),
                ('student_id', models.ForeignKey(to='basicInfo.student')),
            ],
        ),
        migrations.CreateModel(
            name='takeup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('course_id', models.ForeignKey(to='basicInfo.course')),
                ('room_id', models.ForeignKey(to='basicInfo.room')),
            ],
        ),
        migrations.CreateModel(
            name='teach',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('course_id', models.ForeignKey(related_name='college_id_1', to='basicInfo.course')),
            ],
        ),
        migrations.CreateModel(
            name='time',
            fields=[
                ('time_id', models.AutoField(primary_key=True, serialize=False)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('day', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='work',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('college_id', models.ForeignKey(to='basicInfo.college')),
            ],
        ),
        migrations.CreateModel(
            name='attrib',
            fields=[
                ('account_id', models.ForeignKey(primary_key=True, serialize=False, to='basicInfo.account')),
                ('nickname', models.CharField(max_length=40)),
                ('picture', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('exp', models.IntegerField(null=True)),
                ('coin', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('teacher_id', models.ForeignKey(primary_key=True, serialize=False, related_name='teacherId', to='basicInfo.account')),
                ('name', models.CharField(max_length=20)),
                ('teacher_title', models.CharField(max_length=10, default='lecturer')),
                ('teacher_department', models.CharField(max_length=40)),
                ('teacher_management', models.CharField(max_length=40, null=True)),
                ('teacher_mail', models.EmailField(max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='takeup',
            name='time_id',
            field=models.ForeignKey(to='basicInfo.time'),
        ),
        migrations.AddField(
            model_name='quit',
            name='student_id',
            field=models.ForeignKey(to='basicInfo.student'),
        ),
        migrations.AlterUniqueTogether(
            name='minor',
            unique_together=set([('studnet_id', 'discipline_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='major',
            unique_together=set([('studnet_id', 'discipline_id')]),
        ),
        migrations.AddField(
            model_name='log',
            name='operation_id',
            field=models.ForeignKey(to='basicInfo.operation'),
        ),
        migrations.AddField(
            model_name='learn',
            name='student_id',
            field=models.ForeignKey(to='basicInfo.student'),
        ),
        migrations.AddField(
            model_name='examination',
            name='student_id',
            field=models.ForeignKey(to='basicInfo.student'),
        ),
        migrations.AddField(
            model_name='examination',
            name='takeup_id',
            field=models.ForeignKey(to='basicInfo.takeup'),
        ),
        migrations.AddField(
            model_name='evaluate',
            name='student_id',
            field=models.ForeignKey(to='basicInfo.student'),
        ),
        migrations.AddField(
            model_name='belong',
            name='college_id',
            field=models.ForeignKey(to='basicInfo.college'),
        ),
        migrations.AddField(
            model_name='belong',
            name='major_id',
            field=models.ForeignKey(to='basicInfo.major'),
        ),
        migrations.AddField(
            model_name='assist',
            name='course_id',
            field=models.ForeignKey(to='basicInfo.course'),
        ),
        migrations.AddField(
            model_name='assist',
            name='student_id',
            field=models.ForeignKey(to='basicInfo.student'),
        ),
        migrations.AddField(
            model_name='apply',
            name='course_id',
            field=models.ForeignKey(to='basicInfo.course'),
        ),
        migrations.AddField(
            model_name='apply',
            name='student_id',
            field=models.ForeignKey(to='basicInfo.student'),
        ),
        migrations.AddField(
            model_name='work',
            name='teacher_id',
            field=models.ForeignKey(to='basicInfo.teacher'),
        ),
        migrations.AddField(
            model_name='teach',
            name='teacher_id',
            field=models.ForeignKey(related_name='teacher_id_1', to='basicInfo.teacher'),
        ),
        migrations.AddField(
            model_name='takeup',
            name='teacher_id',
            field=models.ForeignKey(to='basicInfo.teacher'),
        ),
        migrations.AlterUniqueTogether(
            name='suspend',
            unique_together=set([('student_id', 'course_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='quit',
            unique_together=set([('student_id', 'course_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='pre',
            unique_together=set([('tmp_course_id', 'pre_course_id')]),
        ),
        migrations.AddField(
            model_name='master',
            name='teacher_id',
            field=models.ForeignKey(to='basicInfo.teacher'),
        ),
        migrations.AlterUniqueTogether(
            name='learn',
            unique_together=set([('student_id', 'course_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='examination',
            unique_together=set([('student_id', 'takeup_id', 'position')]),
        ),
        migrations.AddField(
            model_name='evaluate',
            name='teacher_id',
            field=models.ForeignKey(to='basicInfo.teacher'),
        ),
        migrations.AlterUniqueTogether(
            name='belong',
            unique_together=set([('major_id', 'college_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='assist',
            unique_together=set([('student_id', 'course_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='apply',
            unique_together=set([('student_id', 'course_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='work',
            unique_together=set([('teacher_id', 'college_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='teach',
            unique_together=set([('teacher_id', 'course_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='takeup',
            unique_together=set([('course_id', 'time_id', 'room_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='master',
            unique_together=set([('teacher_id', 'college_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='evaluate',
            unique_together=set([('student_id', 'teacher_id')]),
        ),
    ]
