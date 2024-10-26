from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


def showPosts(request):
    post_about_Danny = Post.objects.get(id=1)
    content = {
        'title': post_about_Danny.title,
        'likes': post_about_Danny.likes,
        'body': post_about_Danny.body,
    }
    return render(request, 'first_page.html', content)
