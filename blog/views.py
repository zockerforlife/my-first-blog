from django.shortcuts import render


def post_list(request, template='blog/post_list.html'):
    context = {
        'page': {
            'title': 'JobUFO\'s Blog'
        },
        'author': 'Mighty Frank'
    }
    return render(request, template, context)
