from django.db import models
from django.contrib.auth.models import AbstractUser
from main.models import Currency


class Consumer(AbstractUser):

    email = models.EmailField(unique=True)
    default_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, default=9624)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Consumer'
        verbose_name_plural = 'Consumers'

class CostGroup(models.Model):
    id = models.AutoField(primary_key=True)
    cost_group_name = models.CharField(max_length=255)
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)

    def __str__(self):
        return self.cost_group_name

    class Meta:
        verbose_name = 'CostGroup'
        verbose_name_plural = 'CostGroups'

class CostRecord(models.Model):
    id = models.AutoField(primary_key=True)
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    cost_group = models.ForeignKey(CostGroup, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note for {self.consumer.username}"

    class Meta:
        verbose_name = 'CostRecord'
        verbose_name_plural = 'CostRecords'
