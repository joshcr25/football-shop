from django.test import TestCase, Client
from .models import Product
from django.test import TestCase, Client
from .models import Product
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from django.contrib.auth.models import User

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
        
    def test_product_default_values(self):
        product = Product.objects.create(
            
        )
        self.assertEqual(product.price, 200000)
        self.assertEqual(product.category, "jersey")
        self.assertEqual(product.quantity, 1)
        self.assertEqual(product.year_of_manufacture, 2025)
        self.assertEqual(product.year_of_product, 2025)
        self.assertFalse(product.is_featured)
        
class FootballShopFunctionalTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Create single browser instance for all tests
        cls.browser = webdriver.Edge()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        # Close browser after all tests complete
        cls.browser.quit()

    def setUp(self):
        # Create user for testing
        self.test_user = User.objects.create_user(
            username='testadmin',
            password='testpassword'
        )

    def tearDown(self):
        # Clean up browser state between tests
        self.browser.delete_all_cookies()
        self.browser.execute_script("window.localStorage.clear();")
        self.browser.execute_script("window.sessionStorage.clear();")
        # Navigate to blank page to reset state
        self.browser.get("about:blank")

    def login_user(self):
        """Helper method to login user"""
        self.browser.get(f"{self.live_server_url}/login/")
        username_input = self.browser.find_element(By.NAME, "username")
        password_input = self.browser.find_element(By.NAME, "password")
        username_input.send_keys("testadmin")
        password_input.send_keys("testpassword")
        password_input.submit()

    def test_login_page(self):
        # Test login functionality
        self.login_user()

        # Check if login is successful
        wait = WebDriverWait(self.browser, 120)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        h1_element = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertEqual(h1_element.text, "SaccerBall")

        logout_link = self.browser.find_element(By.PARTIAL_LINK_TEXT, "Logout")
        self.assertTrue(logout_link.is_displayed())

    def test_register_page(self):
        # Test register functionality
        self.browser.get(f"{self.live_server_url}/register/")

        # Check if register page opens
        h1_element = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertEqual(h1_element.text, "Register")

        # Fill register form
        username_input = self.browser.find_element(By.NAME, "username")
        password1_input = self.browser.find_element(By.NAME, "password1")
        password2_input = self.browser.find_element(By.NAME, "password2")

        username_input.send_keys("newuser")
        password1_input.send_keys("complexpass123")
        password2_input.send_keys("complexpass123")
        password2_input.submit()

        # Check redirect to login page
        wait = WebDriverWait(self.browser, 120)
        wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Login"))
        login_h1 = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertEqual(login_h1.text, "Login")

    def test_create_product(self):
        # Test create product functionality (requires login)
        self.login_user()

        # Go to create product page
        add_button = self.browser.find_element(By.PARTIAL_LINK_TEXT, "Add Product")
        add_button.click()

        # Fill form
        name_input = self.browser.find_element(By.NAME, "name")
        description_input = self.browser.find_element(By.NAME, "description")
        category_select = self.browser.find_element(By.NAME, "category")
        thumbnail_input = self.browser.find_element(By.NAME, "thumbnail")
        brand_input = self.browser.find_element(By.NAME, "brand")
        is_featured_checkbox = self.browser.find_element(By.NAME, "is_featured")

        name_input.send_keys("Test Product Name")
        description_input.send_keys("Test product description for selenium testing")
        thumbnail_input.send_keys("https://media.istockphoto.com/id/1316134499/photo/a-concept-image-of-a-magnifying-glass-on-blue-background-with-a-word-example-zoom-inside-the.jpg?s=612x612&w=0&k=20&c=sZM5HlZvHFYnzjrhaStRpex43URlxg6wwJXff3BE9VA=")
        brand_input.send_keys("Test")

        # Set category (select 'jersey' from dropdown)

        select = Select(category_select)
        select.select_by_value("jersey")

        # Check is_featured checkbox
        is_featured_checkbox.click()

        # Submit form
        name_input.submit()

        # Check if returned to main page and product appears
        wait = WebDriverWait(self.browser, 120)
        wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "SaccerBall"))
        h1_element = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertEqual(h1_element.text, "SaccerBall")

        # Check if product name appears on page
        wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Test Product Name")))
        product_name = self.browser.find_element(By.PARTIAL_LINK_TEXT, "Test Product Name")
        self.assertTrue(product_name.is_displayed())

    def test_product_detail(self):
        # Test product detail page

        # Login first because of @login_required decorator
        self.login_user()

        # Create product for testing
        product = Product.objects.create(
            name="Detail Test Product 2",
            description="Description for detail testing",
            brand="Test",
            user=self.test_user
        )

        # Open product detail page
        self.browser.get(f"{self.live_server_url}/product/{product.id}/")

        # Check if detail page opens correctly
        self.assertIn("Detail Test Product", self.browser.page_source)
        self.assertIn("Description for detail testing", self.browser.page_source)

    def test_logout(self):
        # Test logout functionality
        self.login_user()

        # Click logout button - text is inside button, not link
        logout_button = self.browser.find_element(By.XPATH, "//button[contains(text(), 'Logout')]")
        logout_button.click()

        # Check if redirected to login page
        wait = WebDriverWait(self.browser, 120)
        wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Login"))
        h1_element = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertEqual(h1_element.text, "Login")

    def test_filter_main_page(self):
        # Test filter functionality on main page
        #         
        # Create product for testing
        Product.objects.create(
            name="My Test Product",
            description="My product description",
            brand="mine",
            user=self.test_user
        )
        Product.objects.create(
            name="Other User Product", 
            description="Other product description",
            brand="others",
            user=self.test_user  # Same user for simplicity
        )

        self.login_user()

        # Test filter "All Articles"
        wait = WebDriverWait(self.browser, 120)
        wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "All Products")))
        all_button = self.browser.find_element(By.PARTIAL_LINK_TEXT, "All Products")
        all_button.click()
        self.assertIn("My Test Product", self.browser.page_source)
        self.assertIn("Other User Product", self.browser.page_source)

        # Test filter "My Articles"  
        my_button = self.browser.find_element(By.PARTIAL_LINK_TEXT, "My Products")
        my_button.click()
        self.assertIn("My Test Product", self.browser.page_source)