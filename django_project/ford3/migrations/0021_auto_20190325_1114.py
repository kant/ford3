# Generated by Django 2.1.7 on 2019-03-25 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ford3', '0020_auto_20190322_1103'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campus',
            old_name='provider_id',
            new_name='provider',
        ),
        migrations.RenameField(
            model_name='qualification',
            old_name='campus_id',
            new_name='campus',
        ),
        migrations.RenameField(
            model_name='qualification',
            old_name='sub_field_of_study_id',
            new_name='sub_field_of_study',
        ),
        migrations.AlterField(
            model_name='campus',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
