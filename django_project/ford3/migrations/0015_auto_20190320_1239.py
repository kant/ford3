# Generated by Django 2.1.7 on 2019-03-20 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ford3', '0014_auto_20190320_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualificationentrancerequirementsubject',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='qualificationentrancerequirementsubject',
            name='required',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
