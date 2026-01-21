from blog.data import posts
from django.shortcuts import render

# Create your views here.

def blog(request):
    print('blog')

    context = {
    'posts': posts
    }

    return render(
        request=request,
        template_name='blog/index.html',
        context=context,
    )

def post(request, id):
    print('post', id)

    context = {
    'posts': posts
    }

    return render(
        request=request,
        template_name='blog/index.html',
        context=context,
    )



def example(request):
    print('example')

    context = {
    'text': 'Welcome to the example',
    'title': 'Welcome to the example',

}
    
    return render(
        request=request,
        template_name='blog/example.html',
        context=context,
    )
