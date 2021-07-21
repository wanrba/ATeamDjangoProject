from django.shortcuts import render

# Create your views here.
def defaultPage(request) :
    return render(request, "index.html")