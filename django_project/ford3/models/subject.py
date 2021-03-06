from django.db import models
from ford3.models.secondary_institution_type import SecondaryInstitutionType


class Subject(models.Model):
    secondary_institution_types = models.ManyToManyField(
        SecondaryInstitutionType)

    name = models.CharField(
        blank=False,
        null=False,
        help_text='',
        max_length=255)
    description = models.CharField(
        blank=True,
        null=True,
        help_text='',
        max_length=500)

    def __str__(self):
        return self.name
