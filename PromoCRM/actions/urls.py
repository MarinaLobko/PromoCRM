from django.urls import path
from . import views

from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

app_name = 'actions'
urlpatterns = [
    path ('promo/', views.promo_list, name ='promos'),
    path ('approval/', views.approval_list, name = 'approves'),
    path ('new/', views.new_promo, name = 'newpromo'),
    path('promodetails/<int:promo_id>/', views.detail, name='promodetails'),
    path('deletepromo/<int:promo_id>/', views.deletepromosubmition, name='deletepromo'),
    path('deletepromo/<int:promo_id>/conf/', views.deletepromo, name='deletepromoconfirmation'),
    path('editpromo/<int:promo_id>/', views.PromoUpdate.as_view(), name='editpromo'),
]