from django.shortcuts import render, redirect
from django.views import View
from product.models import Product, ImgProduct, Variation, Category, ProductFilters, Brands, ImgProduct, Category 
from django.template.loader import render_to_string
from django.http.response import HttpResponse
# Create your views here.


class HomeView (View):
    def get (self, request):
        return render (request, 'Home/index.html')





class CategoryView (View):
    def get (self, request):
        list_brands = Brands.objects.all()
        list_category = Category.objects.all()
        filters_product = ProductFilters.objects.all()
        title_product = Product.objects.all()
        variation = Variation.objects.all()
        

        context = {"list_category": list_category, "title_product": title_product, "filters_product": filters_product, "list_brands": list_brands, "variation": variation}
        return render (request, 'Category/category.html', context)


class ProductCatView (View):
    def get (self, request, id):
        title_product =  Product.objects.filter(category_id = id)
        list_brands = Brands.objects.all()
        list_category = Category.objects.all()
        filters_product = ProductFilters.objects.all()
        variation = Variation.objects.all()
        context = {"title_product": title_product, "list_category": list_category, "filters_product": filters_product, "list_brands": list_brands, "variation": variation}
        return render (request, 'Category/productCat.html', context)  

cart = {}
def addcart (request):
    if request.is_ajax():
        id = request.POST.get('id')
        num = request.POST.get('num')
        product =  Product.objects.get(id = id)
        variation = Variation.objects.get(product_id = id)
        if id in cart.keys():
            if variation.price_sale != 0:
                itemcart = {
                    'name': product.title,
                    'code': product.code_product,
                    'price': variation.price_sale,
                    'num': int(cart[id]['num']) + 1
                }   
            else:
                itemcart = {
                    'name': product.title,
                    'code': product.code_product,
                    'price': variation.price,
                    'num': int(cart[id]['num']) + 1
                }
        else:
            if variation.price_sale != 0:
                itemcart = {
                    'name': product.title,
                    'code': product.code_product,
                    'price': variation.price_sale,
                    'num': num
                }   
            else:
                itemcart = {
                    'name': product.title,
                    'code': product.code_product,
                    'price': variation.price,
                    'num': num
                }
        cart[id] = itemcart
        request.session['cart'] = cart
        cartInfo = request.session['cart']
        html = render_to_string('Cart/addcart.html', {'cart': cartInfo})
    return HttpResponse(html)

""" def cart (request):
    return ( render, 'Cart/cart.html' ) """

class CartView (View):
    def get (self, request):
        product = Product.objects.all()
        total = 0;
        carts = request.session['cart']
        for key, value in carts.items():
            total += int(value['price'])*int(value['num'])
        context = {"product": product, 'total': total}
        return render (request, 'Cart/cart.html', context) 


class ThongTinView (View):
    def get (self, request):
        return render (request, 'ThongTin/ThongTin.html')

class OrderView (View):
    def get (self, request):
        total = 0;
        carts = request.session['cart']
        for key, value in carts.items():
            total += int(value['price'])*int(value['num'])
        context = {'total': total}
        return render (request, 'Order/order.html', context)


class ProductView (View):
    def get (self, request, id):
        product =  Product.objects.filter(id = id)
        variation = Variation.objects.all()
        img_product = ImgProduct.objects.all()
        category = Category.objects.all()
        context = {"product": product, "img": img_product , "variation": variation, "category":category}
        return render (request, 'Product/product.html', context)



class TestView (View):
    def get (self, request):
        img_product = ImgProduct.objects.all()
        title_product = Product.objects.all()


        context = {"posts": title_product, "img": img_product}
        return render (request, 'test.html',context)