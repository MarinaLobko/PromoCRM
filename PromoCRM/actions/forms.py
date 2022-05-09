from django.forms import ModelForm
from .models import Promo

class PromoForm(ModelForm):
    class Meta:
        model = Promo
        fields = '__all__'
