from django.contrib import admin
from .models import AuctionItem,bid
# Register your models here.
@admin.register(AuctionItem)
class AuctionAdmin(admin.ModelAdmin):
    list_display = ['id','name','category','description','current_price','max_price','image']

@admin.register(bid)
class AuctionAdmin(admin.ModelAdmin):
    list_display = ['bidder_nm','item','bid_amt']

