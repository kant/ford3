# Generated by Django 2.1.7 on 2019-03-20 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ford3', '0004_auto_20190319_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualification',
            name='completion_rate',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='credits_after_completion',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='critical_skill',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='distance_learning',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='duration_in_months',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='full_time',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='green_occupation',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='high_demand_occupation',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='id',
            field=models.AutoField(help_text='Key of qualification', primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='long_description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='nqf_level',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='part_time',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='short_description',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='total_cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='total_cost_comment',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
