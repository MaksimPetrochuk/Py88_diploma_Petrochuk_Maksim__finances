from django.db import models


class Currency(models.Model):
    id = models.AutoField(primary_key=True)
    currency_name = models.CharField(max_length=255)
    alphabetic_code = models.CharField(max_length=3)
    numeric_code = models.PositiveIntegerField()

    def __str__(self):
        return self.currency_name

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'
