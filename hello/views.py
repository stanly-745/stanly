from pickle import FALSE
from pyexpat import model
from django.shortcuts import render,redirect
from django.views import generic
from .models import bill_product, product,bill
from .forms import billform,billproductform
from django.urls import reverse_lazy

def home(request):
    return render(request,'index.html')

class product_lists(generic.ListView):
    model=product

class product_detail(generic.DetailView):
    model=product

class product_add(generic.CreateView):
    model=product
    fields='__all__'

def billgeneration(request):
    bill_obj=billform(request.POST)
    if bill_obj.is_valid():
       bills=bill_obj.save()
       return redirect('calc-sum',pk=bills.bill_num)
    return render(request,'hello/billadd_form.html',{'form':billform})

def calcsum(request,pk):
    bill_obj=bill.objects.get(bill_num=pk)
    products_set=bill_product.objects.filter(bill_item=bill_obj)
    total=2.0
    for product in products_set:
        price=product.billprod.product_price
        qty=product.quantity
        item_sum=price*qty
        total=total+item_sum
    bill_obj.total_sum=total
    bill_obj.save()
    return redirect('bill-detail',pk=bill_obj.bill_num)

def billdetail(request,pk):
    bill_obj=bill.objects.get(bill_num=pk)
    bill_prds=bill_product.objects.filter(bill_item=bill_obj)
    context={
        'bill':bill_obj,
        'products':bill_prds
    }
    return render(request,'hello/bill_detail.html',context)

class product_update(generic.UpdateView):
    model=product
    fields='__all__'
    template_name='hello/product_form.html'


class product_delete(generic.DeleteView):
    model=product 
    success_url=reverse_lazy('products')
    template_name='hello/product_delete.html'

def productsearch(request):
    search_obj=request.GET.get('search')
    result=product.objects.filter(product_name__contains=search_obj)
    if result:
        results=result 
    else:
        results=False
    return render(request,'hello/product_list.html',{'product_list':results})

def bill_prod_add(request,pk):
    billing_form=billproductform(request.POST)
    bill_obj=bill.objects.get(bill_num=pk)
    if billing_form.is_valid():
        billform_obj=billing_form.save(commit=False)
        product_obj=billform_obj.billprod
        qty=billform_obj.quantity
        try :
            bill_info=bill_product.objects.get(bill_item=bill_obj,billprod=product_obj)
            bill_info.quantity=qty
            bill_info.save()
        except bill_product.DoesNotExist:
            bills=billing_form.save(commit=False)
            bills.bill_item=bill_obj
            bills.save()

        return redirect('calc-sum',pk=bill_obj.bill_num)
    return render(request,'hello/billadd_form.html',{'form':billing_form})








