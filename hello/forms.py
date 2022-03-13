from django import forms 
from django.forms import ModelForm
from hello.models import bill ,bill_product

class billform(forms.ModelForm):
	class Meta:
		model=bill 
		fields=['customer_name']


class billproductform(forms.ModelForm):
	class Meta:
		model=bill_product
		fields=['billprod','quantity']
