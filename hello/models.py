
from unicodedata import category
from django.db import models
from django.urls import reverse

# Create your models here.
class productcategory(models.Model):
    category_num=models.AutoField(primary_key=True)
    category_name=models.CharField(max_length=50,help_text="enter category name",verbose_name='Category Name')

    def __str__(self):
            return self.category_name

class product(models.Model):
    product_num=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=50,help_text='',verbose_name='Product Name')
    product_category=models.ForeignKey('productcategory',on_delete=models.SET_NULL,null=True)
    product_price=models.FloatField()

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('product-detail',args=[str(self.product_num)])

   
    def get_update_url(self):
        return reverse('product-update',args=[str(self.product_num)])

    def get_delete_url(self):
        return reverse('product-delete',args=[str(self.product_num)])


class bill(models.Model):
    bill_num=models.AutoField(primary_key=True)
    customer_name=models.CharField(max_length=50,help_text='',verbose_name='Custome Name')
    products=models.ManyToManyField('bill_product')
    total_sum=models.FloatField(default=2.0)

    def __str__(self):
        return self.customer_name

    def get_absolute_url(self):
        return reverse('bill-detail',args=[str(self.bill_num)])

    def add_product(self):
        return reverse('add-bill-product',args=[str(self.bill_num)])


class bill_product(models.Model):
    bill_product_num=models.AutoField(primary_key=True)
    bill_item=models.ForeignKey('bill',on_delete=models.SET_NULL,null=True)
    billprod=models.ForeignKey('product',on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=1,help_text='default is 1')


def __str__(self):
    return self.billprod.product_name
