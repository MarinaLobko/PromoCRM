from django.test import TestCase
from .models import Promo
from django.urls import reverse


class PromoModelTest(TestCase):
    def test_no_promo(self):
        response = self.client.get(reverse('actions:promos'))
        self.assertContains(response, 'No promos avaliable.')
        self.assertQuerysetEqual(response.context['promolist'], [])
