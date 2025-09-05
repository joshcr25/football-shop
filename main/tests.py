from django.test import TestCase, Client
from .models import Product

class MainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/burhan_always_exists/')
        self.assertEqual(response.status_code, 404)

    def test_product_creation(self):
        product = Product.objects.create(name="ALLPRO JERSEY FUTSAL BAJU SEPAK BOLA PRINTING 1 SET BAJU CELANA PRIA WANITA BAJU OLAHRAGA SETELAN SOCCER 06 BLACK RED",
          price=230000,
          category="jersey",
          is_featured=True,
          quantity=1,
          brand="ALLPRO",
          description="Baju olahraga", year_of_manufacture=2024, year_of_product=2024)
        self.assertEqual(product.name, "ALLPRO JERSEY FUTSAL BAJU SEPAK BOLA PRINTING 1 SET BAJU CELANA PRIA WANITA BAJU OLAHRAGA SETELAN SOCCER 06 BLACK RED")
        self.assertEqual(product.price, 230000)
        self.assertEqual(product.category, "jersey")
        self.assertTrue(product.is_featured)
        self.assertEqual(product.description, "Baju olahraga")
        self.assertEqual(product.quantity, 1)
        self.assertEqual(product.brand, "ALLPRO")
        self.assertEqual(product.year_of_manufacture, 2024)
        self.assertEqual(product.year_of_product, 2024)
        
    def test_news_default_values(self):
        product = Product.objects.create(
            
        )
        self.assertEqual(product.price, 200000)
        self.assertEqual(product.category, "jersey")
        self.assertEqual(product.quantity, 1)
        self.assertEqual(product.year_of_manufacture, 2025)
        self.assertEqual(product.year_of_product, 2025)
        self.assertFalse(product.is_featured)
        
        
