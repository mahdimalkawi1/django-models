from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class TestHome(TestCase):
    def test_status_code(self):
        url = reverse('snacklist')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


    def test_home_page_templates(self):
        url = reverse('snacklist')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
