from django.shortcuts import render
from .models import postBlog
from django.core.paginator import Paginator
# Create your views here.

def index(request):
	post_Blog = postBlog.objects.all()
	paginator = Paginator(post_Blog, 1)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request, 'blog/blog.html',{'page_obj':page_obj})

def postDetail(request, id):
	post_Detail = postBlog.objects.get(id = id)
	return render(request, 'blog/postDetail.html',{'post_Detail':post_Detail})