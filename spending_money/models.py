from django.db import models

class Spend(models.Model):
    name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    pay_date = models.DateField()

    def __unicode__(self):
        return self.name
