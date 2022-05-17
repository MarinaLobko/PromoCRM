from django.test import TestCase
# from .models import Promo
from django.urls import reverse


class PromoModelTest(TestCase):
    def test_no_promo_to_show_details(self):
        response = self.client.get(reverse('actions:details'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Promo you are trying to get does not exist!')
        self.assertQuerysetEqual(response.context['promo_id'], [])