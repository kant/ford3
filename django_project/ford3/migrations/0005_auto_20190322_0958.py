# Generated by Django 2.1.5 on 2019-03-22 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ford3', '0004_auto_20190321_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='admissions_contact_no',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='provider',
            name='logo_url',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='provider',
            name='postal_address',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
