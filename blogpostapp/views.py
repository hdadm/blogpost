from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class BlogListView(ListView):
	model = Post
	template_name = "blogpostapp/home.html"


class BlogDetailView(DetailView):
	model = Post
	template_name = "blogpostapp/post_detail.html"
