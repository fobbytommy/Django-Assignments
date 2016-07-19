from django.shortcuts import render, redirect
import string
import random
def index(request):
	if ('attempt' in request.session) == False:
		request.session['attempt'] = 1
	request.session['random_word'] = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(14))
	return render(request, 'randomWord/index.html')
def generator(request):
	if request.method == 'POST':
		request.session['attempt'] += 1
		request.session['random_word'] = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(14))
		return redirect('/')
	else:
		return redirect('/')
def reset(request):
	if request.method == 'POST':
		del request.session['attempt']
		del request.session['random_word']
		return redirect('/')
	else:
		return redirect('/')
