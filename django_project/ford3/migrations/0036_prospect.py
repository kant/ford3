# Generated by Django 2.1.7 on 2019-04-30 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ford3', '0035_auto_20190426_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prospect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Prospect first and last name', max_length=150, verbose_name='Name (required)')),
                ('telephone', models.CharField(blank=True, help_text='Prospect telephone number', max_length=150)),
                ('email', models.EmailField(help_text='Prospect email address', max_length=254, verbose_name='Email (required)')),
            ],
        ),
    ]