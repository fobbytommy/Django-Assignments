from django.shortcuts import render, redirect
from .models import Course, Description, Comment, Course_new, Course_category, User
from django.core.urlresolvers import reverse
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
	return redirect(reverse('course_index'))

def destroy(request, id):
	if request.method == "GET":
		context = {
			'course': Course.objects.get(id=id)
		}
		return render(request, 'courses/delete.html', context)
	elif request.method == "POST":
		Course.objects.get(id=id).delete()
		return redirect(reverse('course_index'))

def comment(request, id):
	if request.method == "GET":
		context = {
			'course': Course.objects.get(id=id)
		}
		return render(request, 'courses/comment.html', context)
	elif request.method == "POST":
		course = Course.objects.get(id=id)
		Comment.objects.create(comment=request.POST['comment'], course=course)
		return redirect(reverse('course_comment', args=id))

def add_user(request):
	users = User.objects.all()
	categories = Course_category.objects.all()
	courses = Course_new.objects.raw('SELECT courses_course_new.id, courses_course_category.course_number, courses_course_category.title, COUNT(courses_course_new.user_id) AS user_counter FROM courses_course_new JOIN courses_course_category ON courses_course_new.course_category_id = courses_course_category.id GROUP BY courses_course_category.course_number')

	context = {
		'users': users,
		'categories': categories,
		'courses': courses
	}

	return render(request, 'courses/add_user.html', context)

def add_process(request):
	if request.method == "POST":
		user_id = int(request.POST['user'])
		category_id = int(request.POST['category'])
		Course_new.objects.create(user_id = user_id, course_category_id = category_id)
	else:
		pass
	return redirect(reverse('course_add_user'))
