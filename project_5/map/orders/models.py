from django.db import models



class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    prod_id = models.IntegerField(null=True,blank=True)
    user_id = models.IntegerField(null=True,blank=True)
    order_items = models.IntegerField(null=True,blank=True)
    order_total = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)

    def __str__(self):
        return " User = " +str(self.user_id)+", Product id = "+str(self.prod_id)+", Order id = "+str(self.order_id)

