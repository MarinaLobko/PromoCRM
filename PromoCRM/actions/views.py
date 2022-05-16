from django.shortcuts import render, redirect,get_object_or_404
from .models import Promo
from django.http import HttpResponse, Http404
from .forms import PromoForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView



# class PromoUpdate(UpdateView):
#     model = Promo
#     template_name = 'actions/editpromo.html'
#     fields = '__all__'
#     def get_success_url(self):
#         return reverse("actions:promodetails", args=(self.object.id,))

@login_required(login_url=reverse_lazy('identif:login'))
def promo_list(request):
    # user = request.user.username
    # if user != "mari_lobko":
    #     return redirect('actions:newpromo')
    # else:
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


# @login_required(login_url=reverse_lazy('identif:login'))
# def editpromo(request, promo_id):
#     promo = Promo.objects.get(id=promo_id)
#     form = PromoForm(request.POST)
#     if form.is_valid():
#         form.save()
#     return render(request, "actions/promodetails.html", {
#         "promo": promo})