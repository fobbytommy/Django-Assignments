from django.shortcuts import render
from time import strftime, localtime
# MVC CONTROLLER!!!
def index(request):
	current_time = { 'time': strftime('%b %d, %Y %I:%M %p', localtime()) }
	return render(request, 'timedisplay/index.html', current_time)
