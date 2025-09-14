from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "category", "thumbnail", "quantity", "brand", "year_of_manufacture", "year_of_product", "is_featured"]