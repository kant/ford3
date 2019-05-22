# Generated by Django 2.1.7 on 2019-05-15 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ford3', '0041_merge_20190507_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campusevent',
            name='http_link',
            field=models.URLField(blank=True, help_text='A link to a web page containing additional details regarding this event', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='saqaqualification',
            name='name',
            field=models.CharField(help_text='The name of the qualification as approved by SAQA', max_length=255, null=True),
        ),
    ]