from django.db import models


class Aircompany(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=2)

    class Meta:
        verbose_name = 'Aircompany'
        verbose_name_plural = 'Aircompanies'

