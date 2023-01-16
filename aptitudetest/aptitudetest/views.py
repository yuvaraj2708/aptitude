from django.shortcuts import render

# pass id attribute from urls
def home(request):
		
	return render(request, "home.html")
