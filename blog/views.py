from django.shortcuts import render
from django.utils import timezone
from .models import Post

'''

def post_list(request, template='blog/post_list.html'):
    
   context = {
        'page': {
            'title': 'JobUFO\'s Blog'
        },
        'author': 'Mighty Frank'
    }

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, template, context))  


'''

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
