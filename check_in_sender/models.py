# import datetime

from django.db import models
# from django.utils import timezone


class Aircompany(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2)

    class Meta:
        verbose_name = 'Aircompany'
        verbose_name_plural = 'Aircompanies'


class Traveller(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)


class CheckIn(models.Model):
    aircompany = models.ForeignKey(Aircompany, on_delete=models.CASCADE)
    traveller = models.ForeignKey(Traveller, on_delete=models.CASCADE)
    date_time = models.DateTimeField('check-in date')
    status = models.CharField(max_length=10)

    # def check_in_date(self):
    # return self.date_time >= timezone.now() + datetime.timedelta(days=2)


class Email(models.Model):
    template_path = models.CharField(max_length=255)
    content = models.TextField()


class EmailTraveller(models.Model):
    email = models.ForeignKey(Email, on_delete=models.CASCADE)
    traveller = models.ForeignKey(Traveller, on_delete=models.CASCADE)
