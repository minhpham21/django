from django.db import models

# Create your models here.
# Title         : Tiêu đề
# Product       : Sản phẩm
# Category      : Loại sản phẩm
# Slug          : Đường dẫn sản phẩm
# Description   : Mô tả
# Price         : Giá tiền
# Active        : Trạng thái (Còn/hết)
# Inventory     : Hàng tồn kho 
# Variation     : Thay đổi




#NHÃN HIỆU
class Brands (models.Model):
    title = models.CharField(default = '', max_length = 100)

    def __str__(self):
        return self.title





#DANH MỤC SẢNH PHẨM
class ProductFilters (models.Model):
    title = models.CharField(default = '', max_length = 100, null = True)

    def __str__(self):
            return self.title





 # LOẠI SẢN PHẨM
class Category (models.Model):
    title = models.CharField(default = '', max_length = 100)
    slug = models.SlugField(max_length = 100)
    description = models.TextField(default = '')
    active = models.BooleanField(default = True)
    product_filters = models.ForeignKey(ProductFilters, on_delete=models.CASCADE)
    product_brands = models.ForeignKey(Brands, on_delete=models.CASCADE)

    def __str__(self):
        return self.title





 # SẢN PHẨM
class Product (models.Model):
    code_product = models.CharField(default = '', max_length = 255)
    title  = models.CharField(default = '', max_length = 255)
    description = models.TextField(default = '')
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    price = models.IntegerField(default = 0)
    active = models.BooleanField(default = True)

    def __str__(self):
        return self.title





#ẢNH SẢN PHẨM
class ImgProduct(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    img_product = models.CharField(default = '', max_length = 255)

    def __str__(self):
        return str(self.product)

    def __str__(self):
        return str(self.img_product)





# THAY ĐỔI SẢN PHẨM
class Variation (models.Model):
    product = models.ForeignKey (Product, on_delete = models.CASCADE)
    title  = models.CharField ( max_length = 255)
    price = models.IntegerField(default = 0)
    price_sale = models.IntegerField(default = 0)
    active = models.BooleanField(default = True)
    inventory = models.IntegerField (default = 0)
    def __str__(self):
        return self.title