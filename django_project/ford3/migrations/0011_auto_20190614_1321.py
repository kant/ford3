# Generated by Django 2.1.7 on 2019-06-14 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ford3', '0010_auto_20190613_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='assessment',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='provider',
            name='assessment_requirements',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]