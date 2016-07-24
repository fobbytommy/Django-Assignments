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
	Course_new.objects.create(user_id = 1, course_category_id = 1)
	courses = Course_category.objects.raw('SELECT courses_course_category.course_number, courses_course_category.title FROM courses_course_category')
	print Course_new._meta.get_all_field_names()
	print courses
	for course in courses:
		print course
	context = {
		'users': users,
		'categories': categories,
		# 'courses': courses
	}

	# for user in users:
	# 	print user.id
	# 	print user.first_name
	# categories = Course_category.objects.all()
	# for category in categories:
	# 	print category.course_number
	# 	print category.title
	return render(request, 'courses/add_user.html', context)
