from django.urls import path

from blog import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path("blog/", views.all_blogs, name="blogs"),
    path("blog_cat/<int:cid>/", views.all_blogs, name="blog_cat"),
    path("blog/<int:bid>/", views.blog_details, name="blog"),
]