from django.shortcuts import render

# Create your views here.

def blog(request):
    print('blog')
    return render(request=request, template_name='blog/index.html')

def example(request):
    print('example')
    return render(request=request, template_name='blog/example.html')
