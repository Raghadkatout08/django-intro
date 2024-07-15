from django.test import TestCase, SimpleTestCase
from django.urls import reverse

class HomePageTests(SimpleTestCase):
    def test_home_page_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')

class AboutPageTests(SimpleTestCase):
    def test_about_page_status_code(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_about_page_template(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'about.html')

class ContactPageTests(SimpleTestCase):
    def test_contact_page_status_code(self):
        url = reverse('contact')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_contact_page_template(self):
        url = reverse('contact')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'contact.html')