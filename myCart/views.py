from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import CartItem
from cook.models import Food
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
import pdb


@login_required(login_url='/accoutns/login/')
def display_cart(request):
    if request.method == 'GET':
        user_id = request.user.id
        cart_items = CartItem.objects.filter(user_id=user_id)
        count_items = cart_items.count()
        if count_items == 0:
            messages.info(request, "Your bag is empty")

    return render(request, 'mycart/index.html',{'cart_items':cart_items})


@login_required(login_url='/accoutns/login/')
def remove_from_cart(request,id):
    if request.method == 'GET':
        user_id = request.user.id
        cart_item = CartItem.objects.get(pk=id)
        cart_item.delete()
    return display_cart(request)

@login_required(login_url='/accoutns/login/')
def update_quantity(request,id):
    print("this is update_quantity")
    cart_item = CartItem.objects.get(pk=id)
    quantity  = request.GET['quantity']
    cart_item.quantity = quantity
    cart_item.save()

    print("cart id: {}".format(id))
    print(request.GET['quantity'])


    return render(request, 'mycart/index.html', {'id': id, 'quantity': quantity})
