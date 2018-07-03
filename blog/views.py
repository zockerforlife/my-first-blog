from django.shortcuts import render


def post_list(request, template='blog/post_list.html'):
    context = {
        'page': {
            'title': 'JobUFO\'s Blog'
        }
    }
    return render(request, template, context)
