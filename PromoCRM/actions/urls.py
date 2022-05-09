from django.urls import path
from . import views

app_name = 'actions'
urlpatterns = [
    path ('promo/', views.promo_list, name ='promos'),
    path ('approval/', views.approval_list, name = 'approves'),
    path ('new/', views.new_promo, name = 'newpromo'),
    path('promodetails/<int:promo_id>/', views.detail, name='promodetails'),
]