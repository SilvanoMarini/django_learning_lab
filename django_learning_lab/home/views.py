from django.shortcuts import render


# Create your views here.

def home(request):
    print('home')

    context = {
        'text': 'We are at home'
    }

    return render( 
        request=request, 
        template_name='home/index.html', 
        context=context,
    )

