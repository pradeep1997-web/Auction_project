from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AuctionItem(models.Model):
    name=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    description=models.TextField()
    current_price=models.IntegerField()
    max_price=models.IntegerField()
    image=models.ImageField(upload_to='img')

    def __str__(self):
        return self.name


class bid(models.Model):
    bidder_nm=models.ForeignKey(User,on_delete=models.CASCADE)
    item=models.ForeignKey(AuctionItem,on_delete=models.CASCADE)
    bid_amt=models.IntegerField()


