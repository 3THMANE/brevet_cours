# Generated by Django 3.1.4 on 2021-01-09 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursar', '0010_auto_20210108_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bepcar2015',
            name='create',
            field=models.IntegerField(blank=True, null=True, verbose_name='مسابقة'),
        ),
        migrations.AlterField(
            model_name='bepcar2016',
            name='create',
            field=models.IntegerField(blank=True, null=True, verbose_name='مسابقة'),
        ),
        migrations.AlterField(
            model_name='bepcar2017',
            name='create',
            field=models.IntegerField(blank=True, null=True, verbose_name='مسابقة'),
        ),
        migrations.AlterField(
            model_name='bepcar2018',
            name='create',
            field=models.IntegerField(blank=True, null=True, verbose_name='مسابقة'),
        ),
        migrations.AlterField(
            model_name='bepcar2019',
            name='create',
            field=models.IntegerField(blank=True, null=True, verbose_name='مسابقة'),
        ),
        migrations.AlterField(
            model_name='bepcar2020',
            name='create',
            field=models.IntegerField(blank=True, null=True, verbose_name='مسابقة'),
        ),
    ]
