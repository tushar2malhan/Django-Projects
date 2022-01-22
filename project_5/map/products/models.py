from django.db import models



class Product(models.Model):
    prod_id = models.AutoField(primary_key=True)
    prod_name = models.CharField(max_length=100, null=True, blank=True)
    prod_price = models.DecimalField(decimal_places=2, max_digits=10,null=True, blank=True)
    prod_desc = models.TextField(null=True,blank=True)
    prod_avail = models.BooleanField(default=True)

    def __str__(self):
        return self.prod_name
