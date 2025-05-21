from django.test import SimpleTestCase
from django.urls import reverse, resolve
from dashboard.views import home

class DashboardURLTests(SimpleTestCase):
    def test_home_url_resolves(self):
        url = reverse('dashboard:home')
        self.assertEqual(resolve(url).func, home)
