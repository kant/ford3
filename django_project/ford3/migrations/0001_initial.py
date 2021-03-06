# Generated by Django 2.1.5 on 2019-03-07 09:25

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, help_text='The spatial point position of the campus', null=True, srid=4326)),
                ('photo_url', models.CharField(max_length=255, null=True)),
                ('telephone', models.IntegerField(null=True)),
                ('email', models.CharField(max_length=255, null=True)),
                ('max_students_per_year', models.IntegerField(null=True)),
                ('physical_address', models.CharField(max_length=255, null=True)),
                ('postal_address', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FieldOfStudy',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('website', models.CharField(blank=True, max_length=255, null=True)),
                ('logo_url', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('admissions_contact_no', models.CharField(max_length=255)),
                ('postal_address', models.CharField(max_length=255, null=True)),
                ('physical_address', models.CharField(max_length=255, null=True)),
                ('telephone', models.IntegerField(null=True)),
                ('provider_type', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.IntegerField(help_text='Key of qualification', primary_key=True, serialize=False, unique=True)),
                ('qualification_id', models.IntegerField()),
                ('saqa_id', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('short_description', models.CharField(max_length=255)),
                ('long_description', models.CharField(max_length=255)),
                ('nqf_level', models.IntegerField()),
                ('duration_in_months', models.IntegerField()),
                ('full_time', models.BooleanField()),
                ('part_time', models.BooleanField()),
                ('credits_after_completion', models.IntegerField()),
                ('distance_learning', models.BooleanField()),
                ('completion_rate', models.IntegerField(default=0)),
                ('total_cost', models.IntegerField()),
                ('total_cost_comment', models.CharField(max_length=255, null=True)),
                ('critical_skill', models.BooleanField(default=False)),
                ('green_occupation', models.BooleanField(default=False)),
                ('high_demand_occupation', models.BooleanField(default=False)),
                ('campus_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ford3.Campus')),
                ('interests', models.ManyToManyField(to='ford3.Interest')),
                ('occupation_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ford3.Occupation')),
            ],
        ),
        migrations.CreateModel(
            name='QualificationEntranceRequirementSubject',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('minimum_score', models.IntegerField()),
                ('required', models.BooleanField()),
                ('qualification_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ford3.Qualification')),
            ],
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('assessment', models.BooleanField()),
                ('interview', models.BooleanField()),
                ('admission_point_score', models.IntegerField()),
                ('min_qualification', models.IntegerField()),
                ('portfolio', models.BooleanField(default=False)),
                ('portfolio_comment', models.CharField(max_length=255, null=True)),
                ('aps_calculator_link', models.CharField(max_length=255, null=True)),
                ('qualification_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ford3.Qualification')),
            ],
        ),
        migrations.CreateModel(
            name='SecondaryInstitutionType',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SubFieldOfStudy',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('field_of_study_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ford3.FieldOfStudy')),
                ('occupation_id', models.ManyToManyField(to='ford3.Occupation')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('secondary_institution_types', models.ManyToManyField(to='ford3.SecondaryInstitutionType')),
            ],
        ),
        migrations.AddField(
            model_name='qualificationentrancerequirementsubject',
            name='subject_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ford3.Subject'),
        ),
        migrations.AddField(
            model_name='qualification',
            name='sub_field_of_study_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ford3.SubFieldOfStudy'),
        ),
        migrations.AddField(
            model_name='qualification',
            name='subjects',
            field=models.ManyToManyField(through='ford3.QualificationEntranceRequirementSubject', to='ford3.Subject'),
        ),
        migrations.AddField(
            model_name='campus',
            name='provider_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ford3.Provider'),
        ),
    ]
