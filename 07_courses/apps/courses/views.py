from django.shortcuts import render, redirect
from .models import Course, Description, Comment
# Create your views here.
def index(request):
	context = {
		'courses': Course.objects.all()
	}
	return render(request, 'courses/index.html', context)

def add(request):
	if request.method == "POST":
		course = Course.objects.create(name=request.POST['name'])
		Description.objects.create(course=course, description=request.POST['description'])
	return redirect('/')

def destroy(request, id):
	if request.method == "GET":
		context = {
			'course': Course.objects.get(id=id)
		}
		return render(request, 'courses/delete.html', context)
	elif request.method == "POST":
		Course.objects.get(id=id).delete()
		return redirect('/')

def comment(request, id):
	if request.method == "GET":
		context = {
			'course': Course.objects.get(id=id)
		}
		return render(request, 'courses/comment.html', context)
	elif request.method == "POST":
		course = Course.objects.get(id=id)
		Comment.objects.create(comment=request.POST['comment'], course=course)
		return redirect('/courses/comment/{}'.format(id))
