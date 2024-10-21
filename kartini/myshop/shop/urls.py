from django.urls import re_path
from .views import *

urlpatterns = [
    re_path(r'^$', product_list, name='product_list'),
    re_path(r'^dostavka/', dostavka, name='dostavka'),
    re_path(r'^error404/', error404, name='error404'),

    re_path(r'^category/', category, name='category'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        product_detail,
        name='product_detail'),
    re_path(r'^(?P<category_slug>[-\w]+)/$',
        product_list,
        name='product_list_by_category'),


    
    re_path(r'^products/(?P<post_categoryid>\d+)/', products, name='products'),

]


handler404 = 'shop.views.error404'