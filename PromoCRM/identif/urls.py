from django.urls import path
from . import views

app_name = 'identif'
urlpatterns = [
    path ('register/', views.register_page, name = 'reg'),
    path ('', views.login_page, name = 'login'),
    path ('logout/', views.logout_page, name = 'logout'),
]