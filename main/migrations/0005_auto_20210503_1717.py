# Generated by Django 3.1.1 on 2021-05-03 14:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210503_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.task'),
        ),
        migrations.AlterField(
            model_name='connection',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
