from django.shortcuts import render, get_object_or_404
from .models import *
from cart.cart import Cart
from cart.forms import CartAddProductForm



def product_list(request, category_slug=None):
    category = None
    cart = Cart(request)
    page = Pages.objects.get(pk=1)
    categories = Category.objects.all()
    products = Product.objects.filter(available=True).reverse()[0:6]
    slider = Slider.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,'shop/product/list.html',{'cart': cart,'page':page,'category': category,'categories': categories,'products': products,'slider':slider})




def product_detail(request, id, slug ):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart = Cart(request)
    page = Pages.objects.get(pk=5)
    cart_product_form = CartAddProductForm()
    posts = Product.objects.filter(available=True).reverse()[0:4]
    photos = Photos.objects.filter(title=id)
    return render(request, 'shop/product/detail.html', {'cart': cart,'page':page,'product': product,'cart_product_form': cart_product_form,'photos':photos,'posts':posts})







def products(request , post_categoryid):

    page = Pages.objects.get(pk=2)
    cart = Cart(request)
    posts = Product.objects.filter(categoryid=post_categoryid , available=True)
    return render(request, 'shop/product/products.html', {'cart': cart,'page':page,'posts':posts })


def dostavka(request):
    page = Pages.objects.get(pk=3)
    cart = Cart(request)

    return render(request, 'shop/product/dostavka.html', {'cart': cart,'page':page})

def category(request):
    page = Pages.objects.get(pk=4)
    cart = Cart(request)
    category = Category.objects.all()
    return render(request, 'shop/product/products-category.html', {'cart': cart,'page':page , 'category':category})

def error404(request,exeption):
    return render(request,'shop/product/404.html')