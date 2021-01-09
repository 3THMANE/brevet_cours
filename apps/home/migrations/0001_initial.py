# Generated by Django 3.1.3 on 2020-12-06 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=12, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('message', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]