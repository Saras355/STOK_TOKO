from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')
    def test_main_contains_welcome_message(self):
        response = Client().get('/main/')
        #unit test untuk memeriksa apakah ada kalimat Selamat Datang pada halaman main
        self.assertContains(response, 'List Barang Toko Saras')