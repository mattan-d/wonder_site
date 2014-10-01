from django.contrib import admin
from spending_money import models

class SpendAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'cost',
        'pay_date',
        'date',
    ]


admin.site.register(models.Spend, SpendAdmin)
