from django.shortcuts import render,HttpResponse
from .models import AuctionItem,bid
from .forms import Myform,  bid_amount
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.db.models import Min

# Create your views here.

# Home Page function
def home(request):
    data=AuctionItem.objects.all()
    return render(request,'myapp/home.html',{"data":data})

# Auction item details function
def auction(request,pk):
    if request.user.is_authenticated:
        data1=AuctionItem.objects.get(id=pk)
        bid_form = bid_amount()
        return render(request,'myapp/auction.html',{"data":data1,"bid_form":bid_form})
    else:
        messages.warning(request,'Log in First before bid !!')
        return HttpResponseRedirect('/loginf')

# Fill Bid function
def bidfun(request,pk):
    if request.method=="POST":
        data1 = AuctionItem.objects.get(id=pk)
        bidform=bid_amount(request.POST)

        if bidform.is_valid():
            bid_amt=bidform.cleaned_data['bid_amount_field']
            reg=bid(bidder_nm=request.user,item=data1,bid_amt=bid_amt)
            reg.save()
            messages.success(request,"You bid your amount successfully !!!!")
            return HttpResponseRedirect('/')

# Signup function
def register(request):
    if request.method == "POST":
        form = Myform(request.POST)
        if form.is_valid():
            form.save()
            form = Myform()
            messages.success(request,'Registered successfully !!!')
    else:
        form = Myform()
    return render(request,'myapp/sign_in.html',{"form":form})

# Login function
def loginf(request):
    if not request.user.is_authenticated:
        if request.method =="POST":
            form=AuthenticationForm(request=request, data=request.POST)

            if form.is_valid():
                uname = form.cleaned_data['username']
                pwd = form.cleaned_data['password']
                user=authenticate(username=uname, password=pwd)
                if user is not None:
                    login(request,user)
                    messages.success(request,"Login successfully !!!")
                    return HttpResponseRedirect('/')
        else:
            form=AuthenticationForm()
        return render(request,'myapp/login.html',{"form":form})
    else:
        return HttpResponseRedirect('/')

# Logout function
def logoutf(request):
    logout(request)
    messages.success(request,'log out succesfully !!')
    return HttpResponseRedirect('/')


# All Auction function

def bidportal(request):
    if request.user.is_superuser == True:
        res=bid.objects.all()

    else:
        res=None
        messages.error(request,"You are not admin")
        return HttpResponseRedirect('/')

    return render(request,'myapp/bidportal.html',{"res":res})


# Winner Name display
p=[]
def result(request):
    t = []
    res=bid.objects.all()
    list_res=list(res)
    for i in list_res:
        if i.item not in p:
            p.append(i.item)

    for j in p:
        item_nm = bid.objects.filter(item=j).aggregate(Min('bid_amt'))
        min_bid = bid.objects.filter(bid_amt=item_nm['bid_amt__min'])
        t.append(min_bid[0])
    return render(request,'myapp/result.html',{"min_bid":t,"list_item":'list_item'})