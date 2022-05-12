from django.shortcuts import render, redirect,get_object_or_404
from .models import Promo
from django.http import HttpResponse, Http404
from .forms import PromoForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView


class PromoUpdate(UpdateView):
    model = Promo
    template_name = 'actions/editpromo.html'
    fields = '__all__'
    def get_success_url(self):
        return reverse("actions:promodetails", args=(self.object.id,))

@login_required(login_url=reverse_lazy('identif:login'))
def promo_list(request):
    promolist = Promo.objects.order_by ('start_date')
    context = {
        'promolist': promolist,
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
    if request.method == 'POST':
        form = PromoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('actions:promos')
    else:
        form = PromoForm
    return render(request, 'actions/newpromo.html', {'form': form})

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

# @login_required(login_url=reverse_lazy('identif:login'))
# def editpromo(request, promo_id):
#     try:
#         promo = Promo.objects.get(id=promo_id)
#         if request.method == "POST":
#             promo.sku = request.POST.get("sku")
#             promo.client = request.POST.get("client")
#             promo.promo_type = request.POST.get("promo_type")
#             promo.promo_volume = request.POST.get("promo_volume")
#             promo.promo_discount = request.POST.get("promo_discount")
#             promo.start_date = request.POST.get("start_date")
#             promo.end_date = request.POST.get("end_date")
#             promo.percent_this_month = request.POST.get("percent_this_month")
#             promo.percent_next_month = request.POST.get("percent_next_month")
#         else:
#             return render(request, "actions/editpromo.html", {"promo": promo})
#     except Promo.DoesNotExist:
#         raise Http404("Promo you are trying to get does not exist!")
#     return redirect('actions:promos')
