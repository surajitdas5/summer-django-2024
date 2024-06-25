from django.shortcuts import render, HttpResponse, get_object_or_404
from blog.models import Blog, BlogCategory

# Create your views here.
def index(request):
    # return HttpResponse("Hello World!!!")
    return render(request, 'blog/index.html')

def about(request):
    # return HttpResponse("<h1>About Us</h1>")
    return render(request, 'blog/about.html')

def contact(request):
    mobile = 9876556789
    email = "pulseai@gmail.com"
    a = 10
    b = 10
    languages = ['C', 'C++', 'Java', 'Python']
    blog = {
        "title": "Blog Title",
        "author": "John",
        "content": "Blog details"
    }
    students = [
        {"roll": 1, "name": "Smaith", "cgpa": 8.9},
        {"roll": 2, "name": "Sara", "cgpa": 9.9},
        {"roll": 3, "name": "Tom", "cgpa": 9.5},
        {"roll": 4, "name": "Spike", "cgpa": 8.7},
        {"roll": 5, "name": "Jane", "cgpa": 7.9},
    ]
    context = {
        "mob": mobile,
        "email": email,
        "a": a,
        "b" : b,
        'languages': languages,
        'blog': blog,
        'students': students
    }
    return render(request, 'blog/contact.html', context)

def all_blogs(request, cid=0):
    # blogs = Blog.objects.all()
    if cid == 0:
        blogs = Blog.objects.filter(publish=True).order_by('-update_at')
    else:
        blogs = Blog.objects.filter(publish=True, category=cid).order_by('-update_at')
    categories = BlogCategory.objects.all().order_by('category')
    context = {
        'blogs': blogs,
        'categories' : categories
    }
    return render(request, 'blog/blog.html', context)

def blog_details(request, bid):
    # blog = Blog.objects.get(id=bid)
    blog = get_object_or_404(Blog, pk=bid)
    
    context = {
        'blog': blog
    }
    return render(request, 'blog/details.html', context)