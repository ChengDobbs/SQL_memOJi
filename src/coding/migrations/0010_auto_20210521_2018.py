# Generated by Django 3.1.7 on 2021-05-21 12:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coding', '0009_auto_20210521_2012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quesanswerrec',
            name='student',
        ),
        migrations.AddField(
            model_name='quesanswerrec',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.user', verbose_name='学生'),
            preserve_default=False,
        ),
    ]