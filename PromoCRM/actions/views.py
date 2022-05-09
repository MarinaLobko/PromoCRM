from django.shortcuts import render, redirect
from .models import Promo
from django.http import HttpResponse, Http404
from django.views import generic
from .forms import PromoForm
from django.urls import reverse


def promo_list(request):
    promolist = Promo.objects.order_by ('start_date')
    context = {
        'promolist': promolist,
    }
    return render (request= request, template_name = 'actions/promos.html', context = context)

def detail(request, promo_id):
    try:
        promo = Promo.objects.get(id=promo_id)
    except Promo.DoesNotExist:
        raise Http404("Question you are trying to get does not exist!")
    return render(request,'actions/promodetails.html', { 'promo': promo })

def approval_list(request):
    return render (request, 'actions/approves.html')

def new_promo(request):
    if request.method == 'POST':
        form = PromoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('actions:promos')
    else:
        form = PromoForm
    return render(request, 'actions/newpromo.html', {'form': form})