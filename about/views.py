from django.shortcuts import render

def about(request):
	#title = 'About page'
	context = {
	}
	return render(request, 'about.html', {})
