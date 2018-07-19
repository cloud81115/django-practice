from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
	class Meta:
		model=Product
		fields=[
			'title',
			'description',
			'price'

		]

class RawProductForm(forms.Form):
	title 		= forms.CharField(label='')
	description = forms.CharField(
						required=False, 
						widget=forms.Textarea(
								attrs={
									"class":"new-class-name two",
									"rows":20,
									"cols":100
									}
								)
						)
	price = forms.DecimalField(initial=199.99)