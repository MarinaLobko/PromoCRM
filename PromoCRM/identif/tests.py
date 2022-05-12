from django.test import TestCase
from django.urls import reverse
from .forms import CreateUserForm

def create_promo(email):
    email = CreateUserForm(email = email)
    return email

class LoginTest(TestCase):
    def test_not_an_employee(self):
        email = create_promo(email = 'lobkomarina.by@mail.ru')
        response = self.client.get(reverse('identif:reg'))
        self.assertContains(response, 'You are not an Alivaria emloyee!')
        self.assertQuerysetEqual(response.context['email'], [email])