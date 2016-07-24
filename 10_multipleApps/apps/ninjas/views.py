from django.shortcuts import render

def index(request):
	return render(request, 'ninjas/index.html')
def ninjas(request):
	return render(request, 'ninjas/ninjas.html')
def color(request, color):
	context = { 'color': color }
	if color == "blue":
		context['img_url'] = "img/leonardo.jpg"
		context['name'] = "Leonardo"
	elif color == "orange":
		context['img_url'] = "img/michelangelo.jpg"
		context['name'] = "Michelangelo"
	elif color == "red":
		context['img_url'] = "img/raphael.jpg"
		context['name'] = "Raphael"
	elif color == "purple":
		context['img_url'] = "img/donatello.jpg"
		context['name'] = "Donatello"
	else:
		context['img_url'] = "img/notapril.jpg"
		context['name'] = "Megan Fox"
	return render(request, 'ninjas/color.html', context)
