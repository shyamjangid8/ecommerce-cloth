from django.shortcuts import render,get_object_or_404
from category.models import category
# Create your views here.
from .models import Product

def store(request,category_slugs=None):
    categories = None
    products = None
    if category_slugs != None:
        categories = get_object_or_404(category,slug=category_slugs)
        products = Product.objects.filter(category=categories,is_avaiable=True)
        products_counts = products.count()
    else:
        products = Product.objects.all().filter( is_avaiable=True)
        products_counts = products.count()
    context = {
        "products" : products,
        'product_count':products_counts
    }
    return render(request,'store/store.html',context)


def product_detail(request,category_slugs,product_slug):
    try:
        single_product = Product.objects.get(category__slug = category_slugs,slug=product_slug)
    except Exception as e:
        raise e
    context = {
        'single_product':single_product,
    }
    return render(request,'store/product_detail.html',context)