# Generated by Django 3.1.7 on 2021-05-21 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0008_auto_20210521_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quesanswerrec',
            name='ans_status',
            field=models.IntegerField(choices=[(-1, '未知'), (0, '答案正确'), (1, '答案错误'), (2, '运行异常')], default=-1, verbose_name='答案正确性'),
        ),
    ]