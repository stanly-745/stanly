from django.views import View
from hello.models import product
from . import views
from django.urls import path,include

urlpatterns =[
    path('',views.home,name='HOME'),
    path('products/',views.product_lists.as_view(),name='products'),
    path('product/<int:pk>',views.product_detail.as_view(),name='product-detail'),
    path('product/<int:pk>/update',views.product_update.as_view(),name='product-update'),
    path('product/<int:pk>/delete',views.product_delete.as_view(),name='product-delete'),
    path('product/add',views.product_add.as_view(),name='product-add'),
    path('bill/add/',views.billgeneration,name='bill-add'),
    path('bill/sum/<int:pk>',views.calcsum,name='calc-sum'),
    path('bill/<int:pk>',views.billdetail,name='bill-detail'),
    path('search-result/',views.productsearch,name='product-search'),
    path('add-product-in-bill/<int:pk>/',views.bill_prod_add,name='add-bill-product')

    
    
]
    
