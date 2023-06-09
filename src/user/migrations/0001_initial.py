# Generated by Django 3.1.7 on 2022-02-28 05:35

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=100, primary_key=True, serialize=False, verbose_name='电子邮件')),
                ('priority', models.IntegerField(choices=[(0, '学生'), (1, '教师'), (2, '管理员')], default=0, verbose_name='权限等级')),
                ('full_name', models.CharField(max_length=30, verbose_name='真实姓名')),
                ('internal_id', models.CharField(max_length=30, verbose_name='学工号')),
                ('college_name', models.CharField(blank=True, default='计算机学院', max_length=150, verbose_name='学院全称')),
                ('join_status', models.IntegerField(choices=[(0, '名单之外'), (1, '未加入'), (2, '已加入'), (3, '管理员')], default=0, verbose_name='加入状态')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('class_id', models.AutoField(primary_key=True, serialize=False, verbose_name='班级ID')),
                ('class_name', models.CharField(max_length=150, verbose_name='班级名称')),
                ('class_desc', models.CharField(blank=True, max_length=200, null=True, verbose_name='班级描述')),
                ('active', models.BooleanField(default=True, verbose_name='有效状态')),
                ('join_code', models.CharField(max_length=20, unique=True, verbose_name='班级识别码')),
                ('need_list', models.BooleanField(default=True, verbose_name='需要学生清单')),
            ],
            options={
                'verbose_name': '班级',
                'verbose_name_plural': '班级',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('school_id', models.AutoField(primary_key=True, serialize=False, verbose_name='学校ID')),
                ('school_name', models.CharField(default='西北工业大学', max_length=150, unique=True, verbose_name='学校全称')),
                ('school_name_en', models.CharField(default='Northwestern Polytechnical University', max_length=150, unique=True, verbose_name='学校英文全称')),
                ('school_abbr', models.CharField(default='NPU', max_length=50, unique=True, verbose_name='学校英文缩写')),
            ],
            options={
                'verbose_name': '学校',
                'verbose_name_plural': '学校',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user.user')),
            ],
            options={
                'verbose_name': '教师',
                'verbose_name_plural': '教师',
            },
        ),
        migrations.CreateModel(
            name='StudentList',
            fields=[
                ('record_id', models.AutoField(primary_key=True, serialize=False, verbose_name='记录ID')),
                ('full_name', models.CharField(max_length=30, verbose_name='学生姓名')),
                ('internal_id', models.CharField(max_length=30, verbose_name='学号')),
                ('join_status', models.BooleanField(default=False, verbose_name='加入状态')),
                ('classroom', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.classroom', verbose_name='班级')),
            ],
            options={
                'verbose_name': '学生清单',
                'verbose_name_plural': '学生清单',
            },
        ),
        migrations.AddField(
            model_name='classroom',
            name='school',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.school', verbose_name='学校'),
        ),
        migrations.AddField(
            model_name='user',
            name='school',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.school', verbose_name='学校'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user.user')),
                ('classroom', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.classroom', verbose_name='班级')),
            ],
            options={
                'verbose_name': '学生',
                'verbose_name_plural': '学生',
            },
        ),
        migrations.AddField(
            model_name='classroom',
            name='teacher',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.teacher', verbose_name='负责教师'),
        ),
    ]
