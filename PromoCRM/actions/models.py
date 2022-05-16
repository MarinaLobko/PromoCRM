from django.db import models

def get_username(request):
    username = request.user.username
    return username

class Promo(models.Model):
    sku = models.CharField(max_length=200)
    client = models.CharField(max_length=200)
    promo_type = models.CharField(max_length=200)
    promo_volume = models.CharField(max_length=200)
    promo_discount = models.CharField(max_length=200)
    start_date = models.CharField(max_length=200)
    end_date = models.CharField(max_length=200)
    percent_this_month = models.CharField(max_length=200)
    percent_next_month = models.CharField(max_length=200)
    def __str__(self):
        return self.client + " | " + self.sku + " | " + self.start_date + "-" + self.end_date