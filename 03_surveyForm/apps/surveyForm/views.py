from django.shortcuts import render, redirect

def index(request):
	return render(request, 'surveyForm/index.html')
def process(request):
	if request.method == "POST":
		if ('count' in request.session) == False:
			request.session['count'] = 1
		else:
			request.session['count'] += 1
		request.session['name'] = request.POST['name']
		request.session['location'] = request.POST['location']
		request.session['language'] = request.POST['language']
		request.session['comment'] = request.POST['comment']
		return redirect('/result')
	else:
		return redirect('/')
def result(request):
	return render(request, 'surveyForm/result.html')
