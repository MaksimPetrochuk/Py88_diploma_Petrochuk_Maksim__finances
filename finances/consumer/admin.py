from django.contrib import admin
from consumer.models import Consumer, CostGroup, CostRecord


admin.site.register(Consumer)
admin.site.register(CostGroup)
admin.site.register(CostRecord)
