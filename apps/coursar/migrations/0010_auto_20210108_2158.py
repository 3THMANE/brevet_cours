# Generated by Django 3.1.4 on 2021-01-09 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursar', '0009_auto_20210108_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bepcar2015',
            name='status',
            field=models.CharField(choices=[('draft', 'إخفاء'), ('published', 'نشر')], default='draft', max_length=20, verbose_name='حالة'),
        ),
        migrations.AlterField(
            model_name='bepcar2016',
            name='status',
            field=models.CharField(choices=[('draft', 'إخفاء'), ('published', 'نشر')], default='draft', max_length=20, verbose_name='حالة'),
        ),
        migrations.AlterField(
            model_name='bepcar2017',
            name='status',
            field=models.CharField(choices=[('draft', 'إخفاء'), ('published', 'نشر')], default='draft', max_length=20, verbose_name='حالة'),
        ),
        migrations.AlterField(
            model_name='bepcar2018',
            name='status',
            field=models.CharField(choices=[('draft', 'إخفاء'), ('published', 'نشر')], default='draft', max_length=20, verbose_name='حالة'),
        ),
        migrations.AlterField(
            model_name='bepcar2019',
            name='status',
            field=models.CharField(choices=[('draft', 'إخفاء'), ('published', 'نشر')], default='draft', max_length=20, verbose_name='حالة'),
        ),
        migrations.AlterField(
            model_name='bepcar2020',
            name='status',
            field=models.CharField(choices=[('draft', 'إخفاء'), ('published', 'نشر')], default='draft', max_length=20, verbose_name='حالة'),
        ),
    ]
