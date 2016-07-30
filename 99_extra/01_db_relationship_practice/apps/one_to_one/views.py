from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from .models import Blog, Description
# Create your views here.
def index(request):
	context = {
		# 'blogs': Blog.objects.filter(id__in=[3,4,5]).order_by('-created_at')
		# 'blogs': Blog.objects.all().order_by('-created_at')
		# 'blogs': Blog.objects.exclude(id__in=[3, 6, 7]).order_by('-created_at')
		'blogs': Blog.objects.exclude(description__id=3).order_by('-created_at')
	}
	return render(request, "one_to_one/index.html", context)

def process(request):
	if request.method == "POST":
		Blog.blogManager.add_blog(request.POST)
		return redirect(reverse('one_to_one_index'))
