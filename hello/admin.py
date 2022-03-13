from django.contrib import admin
from .models import bill_product, productcategory,product,bill
# Register your models here.

admin.site.register(productcategory)

admin.site.register(product)

admin.site.register(bill)

admin.site.register(bill_product)
