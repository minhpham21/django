from django.contrib import admin
from .models import Product, ImgProduct, Category, Variation, ProductFilters, Brands

# Register your models here.
admin.site.register(Product)
admin.site.register(ImgProduct)
admin.site.register(Category)
admin.site.register(Variation)
admin.site.register(ProductFilters)
admin.site.register(Brands)