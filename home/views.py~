from django.shortcuts import render
from .forms import Newsletter

def home(request):
	
	form = Newsletter(request.POST or None)
	
	if form.is_valid():
		instance = form.save(commit = False)
		print instance.email
		instance.save()
	
	context = {
	#	"title": title,
		"form":form,
	}
	return render(request, 'home.html', context)
