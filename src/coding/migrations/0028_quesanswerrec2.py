# Generated by Django 3.1.7 on 2022-02-06 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0027_delete_quesanswerrec2'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuesAnswerRec2',
            fields=[
                ('rec_id', models.AutoField(primary_key=True, serialize=False, verbose_name='记录ID')),
            ],
            options={
                'verbose_name': '题目作答记录(*)',
                'verbose_name_plural': '题目作答记录(*)',
            },
        ),
    ]
