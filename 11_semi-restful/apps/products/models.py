from __future__ import unicode_literals

from django.db import models


class ProductManager(models.Manager):
	def new(self, product_info):
		name = product_info['name']
		description = product_info['description']
		price = product_info['price']
		errors = []
		if len(name) < 1:
			errors.append("Please specify the product's name.")
		if len(description) < 1:
			errors.append("Please specify the product's description.")
		elif len(description) > 500:
			errors.append("Please keep the description short! No longer than 500 characters.")
		if len(price) < 1:
			errors.append("Please specify the product's price.")

		if errors:
			return (False, errors)
		else:
			Product.objects.create(name = name, description = description, price = float(price))
			return (True, "Succefully added a new product to the list!")

	def edit(self, product_info, id):
		name = product_info['name']
		description = product_info['description']
		price = product_info['price']
		u = Product.objects.get(id=id)
		errors = []
		if (len(name) > 1 and len(name) < 100):
			u.name = name
		else:
			errors.append("Updated product name is too long!")
		if (len(description) > 1 and len(description) < 500):
			u.description = description
		else:
			errors.append("Updated product description is too long!")
		if len(price) > 1:
			u.price = float(price)
		u.save()

		if errors:
			return (False, errors)
		else:
			return (True, "Succefully updated a product to the list!")

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(max_length=500)
	price = models.FloatField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	# *************************
	# Connect an instance of ProductManager to our Product model!
	productManager = ProductManager()
	# Re-adds objects as a manager (so all the normal ORM literature matches)
	objects = models.Manager()
	# *************************
