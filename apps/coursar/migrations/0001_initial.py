# Generated by Django 3.1.3 on 2020-11-24 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bepcar2015',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=100, unique=True, verbose_name='رابط')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='المادة')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='الموضوع')),
                ('text', models.TextField(verbose_name='النص')),
                ('create', models.DateTimeField(auto_now_add=True, null=True, verbose_name='وقت النشر')),
            ],
        ),
        migrations.CreateModel(
            name='Bepcar2016',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=100, unique=True, verbose_name='رابط')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='المادة')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='الموضوع')),
                ('text', models.TextField(verbose_name='النص')),
                ('create', models.DateTimeField(auto_now_add=True, null=True, verbose_name='وقت النشر')),
            ],
        ),
        migrations.CreateModel(
            name='Bepcar2017',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=100, unique=True, verbose_name='رابط')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='المادة')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='الموضوع')),
                ('text', models.TextField(verbose_name='النص')),
                ('create', models.DateTimeField(auto_now_add=True, null=True, verbose_name='وقت النشر')),
            ],
        ),
        migrations.CreateModel(
            name='Bepcar2018',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=100, unique=True, verbose_name='رابط')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='المادة')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='الموضوع')),
                ('text', models.TextField(verbose_name='النص')),
                ('create', models.DateTimeField(auto_now_add=True, null=True, verbose_name='وقت النشر')),
            ],
        ),
        migrations.CreateModel(
            name='Bepcar2019',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=100, unique=True, verbose_name='رابط')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='المادة')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='الموضوع')),
                ('text', models.TextField(verbose_name='النص')),
                ('create', models.DateTimeField(auto_now_add=True, null=True, verbose_name='وقت النشر')),
            ],
        ),
        migrations.CreateModel(
            name='Bepcar2020',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=100, unique=True, verbose_name='رابط')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='المادة')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='الموضوع')),
                ('text', models.TextField(verbose_name='النص')),
                ('create', models.DateTimeField(auto_now_add=True, null=True, verbose_name='وقت النشر')),
            ],
        ),
    ]