from django.shortcuts import render, redirect,get_object_or_404
from .models import Promo
from django.http import HttpResponse, Http404
from .forms import PromoForm, SearchForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import SearchVector
import csv



@login_required(login_url=reverse_lazy('identif:login'))
def promo_list(request):
    form = SearchForm()
    promolist = Promo.objects.order_by ('start_date')
    context = {
        'promolist': promolist,
        'form':form
    }
    return render (request= request, template_name = 'actions/promos.html', context = context)

@login_required(login_url=reverse_lazy('identif:login'))
def detail(request, promo_id):
    try:
        promo = Promo.objects.get(id=promo_id)
    except Promo.DoesNotExist:
        raise Http404("Promo you are trying to get does not exist!")
    return render(request,'actions/promodetails.html', { 'promo': promo })


@login_required(login_url=reverse_lazy('identif:login'))
def approval_list(request):
    return render (request, 'actions/approves.html')

@login_required(login_url=reverse_lazy('identif:login'))
def new_promo(request):
    error = False
    if request.method == 'POST':
        form = PromoForm(request.POST)
        if form.is_valid():
            percent_this_month = int(request.POST.get('percent_this_month'))
            percent_next_month = int(request.POST.get('percent_next_month'))
            if percent_this_month+percent_next_month == 100:
                form.save()
                return redirect('actions:promos')
            else:
                error = "Percent sum isn't 100%!"
    else:
        form = PromoForm()
    return render(request, 'actions/newpromo.html', {'form': form, 'error':error})

@login_required(login_url=reverse_lazy('identif:login'))
def deletepromosubmition(request, promo_id):
    try:
        promo = Promo.objects.get(id=promo_id)
    except Promo.DoesNotExist:
        raise Http404("Promo you are trying to get does not exist!")
    return render(request,'actions/deletepromo.html', { 'promo': promo })

@login_required(login_url=reverse_lazy('identif:login'))
def deletepromo(request, promo_id):
    try:
        promo = Promo.objects.get(id=promo_id)
        promo.delete()
    except Promo.DoesNotExist:
        raise Http404("Promo you are trying to get does not exist!")
    return redirect('actions:promos')

@login_required(login_url=reverse_lazy('identif:login'))
def editpromo(request, pk):
    promo = Promo.objects.get(pk=pk)
    form = PromoForm(instance=promo)
    if request.method == "POST":
        form = PromoForm(request.POST, instance=promo)
        if form.is_valid():
            form.save()
            return redirect('actions:promodetails', promo.pk)
    else:
        return render(request, "actions/editpromo.html", {
            "promo": promo,
            "form" : form})

@login_required(login_url=reverse_lazy('identif:login'))
def search_promo(request):
    form = SearchForm()
    query = None
    results = []
    if "query" in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_vector = SearchVector('sku','client')
            results = Promo.objects.annotate(search=search_vector).filter(search=query)
    return render(request, 'actions/search.html', {'form':form , 'query':query, 'results':results})

def exportcsv(request):
    promo = Promo.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=promo.csv'
    writer = csv.writer(response)
    writer.writerow(['sku','client', 'promo_type', 'promo_volume', 'promo_discount','start_date', 'end_date', 'percent_this_month', 'percent_this_month'])
    promos = promo.values_list('sku','client', 'promo_type', 'promo_volume', 'promo_discount','start_date', 'end_date', 'percent_this_month', 'percent_this_month')
    for element in promos:
        writer.writerow(element)
    return response