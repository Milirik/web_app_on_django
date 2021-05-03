# Generated by Django 3.1.1 on 2021-05-03 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210503_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attributes',
            name='astronomy',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', max_length=50, verbose_name='Астрономия'),
        ),
        migrations.AlterField(
            model_name='attributes',
            name='biology',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', max_length=50, verbose_name='Биология'),
        ),
        migrations.AlterField(
            model_name='attributes',
            name='chemistry',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', max_length=50, verbose_name='Химия'),
        ),
        migrations.AlterField(
            model_name='attributes',
            name='ecology',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', max_length=50, verbose_name='Экология'),
        ),
        migrations.AlterField(
            model_name='attributes',
            name='geography',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', max_length=50, verbose_name='География'),
        ),
        migrations.AlterField(
            model_name='attributes',
            name='history',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', max_length=50, verbose_name='История'),
        ),
        migrations.AlterField(
            model_name='attributes',
            name='literature',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', max_length=50, verbose_name='Литература'),
        ),
        migrations.AlterField(
            model_name='attributes',
            name='mathematics',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', max_length=50, verbose_name='Математика'),
        ),
        migrations.AlterField(
            model_name='attributes',
            name='music',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', max_length=50, verbose_name='Музыка'),
        ),
        migrations.AlterField(
            model_name='attributes',
            name='physics',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', max_length=50, verbose_name='Физика'),
        ),
        migrations.AlterField(
            model_name='attributes',
            name='russian',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', max_length=50, verbose_name='Руссский язык'),
        ),
        migrations.AlterField(
            model_name='attributes',
            name='technology',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', max_length=50, verbose_name='Технология'),
        ),
    ]