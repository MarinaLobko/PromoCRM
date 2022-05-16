from django.forms import ModelForm, Form, CharField
from .models import Promo

class PromoForm(ModelForm):
    class Meta:
        model = Promo
        fields = '__all__'

class SearchForm(Form):
    query = CharField()
