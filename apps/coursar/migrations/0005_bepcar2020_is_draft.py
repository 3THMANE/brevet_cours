# Generated by Django 3.1.4 on 2021-01-09 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursar', '0004_auto_20201203_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='bepcar2020',
            name='is_draft',
            field=models.BooleanField(default=False),
        ),
    ]
