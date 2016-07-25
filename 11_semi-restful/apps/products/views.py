from django.shortcuts import render, redirect
from .models import Product
from django.contrib import messages
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
	context = {
		'products': Product.objects.all()
	}
	return render(request, 'products/index.html', context)

def show(request, id):
	context = {
		'product': Product.objects.get(id = id)
	}
	return render(request, 'products/show.html', context)

def new(request):
	if request.method == "GET":
		return render(request, 'products/new.html')
	elif request.method == "POST":
		val_result = Product.productManager.new(request.POST)
		request.session['new_product'] = request.POST
		if val_result[0] == False:
			for error in val_result[1]:
				messages.error(request, error)
			return redirect(reverse('products_new'))
		else: # if validation is OKAY (TRUE)
			messages.success(request, val_result[1])
			del request.session['new_product']
			return redirect(reverse('products_index'))
		return render(request, 'products/new.html')

def edit(request, id):
	if request.method == "GET":
		context = {
			'product': Product.objects.get(id = id)
		}
		return render(request, 'products/edit.html', context)
	else: # if request is POST
		val_result = Product.productManager.edit(request.POST, id)
		if val_result[0] == False:
			for error in val_result[1]:
				messages.error(request, error)
			# return redirect(reverse('products_edit', id))
			return redirect('/products/edit/{}'.format(id))
		else: # if validation is OKAY (TRUE)
			messages.success(request, val_result[1])
			return redirect(reverse('products_index'))

def destroy(request, id):
	if request.method == "POST":
		Product.objects.get(id=id).delete() # deleting from the database
		messages.success(request,"Successfully deleted a product from the list!")
		return redirect(reverse('products_index'))
	else:
		messages.success(request,"Nothing happend!")
		return redirect(reverse('products_index'))
