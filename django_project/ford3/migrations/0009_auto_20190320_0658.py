# Generated by Django 2.1.7 on 2019-03-20 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ford3', '0008_auto_20190320_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirement',
            name='aps_calculator_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
