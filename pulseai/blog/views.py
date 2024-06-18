from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World!!!")

def about(request):
    return HttpResponse("<h1>About Us</h1>")
