from blog.data import posts
from django.http import Http404, HttpRequest
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

def post(request: HttpRequest, post_id: int):
    print('post', post_id)
    found_post = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break


    if found_post is None:
        raise Http404('Post not found')


    context = {
    'post': found_post,
    'title': found_post['title'] + ' - ',
    }

    return render(
        request=request,
        template_name='blog/post.html',
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
