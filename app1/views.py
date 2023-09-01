from django.shortcuts import render

# from django.shortcuts import render
from django.http import request, HttpResponse



from .models import Post


def createpost(request):
        if request.method == 'POST':
            if request.POST.get('phone_number') and request.POST.get('email'):
                post=Post()
                post.first_name= request.POST.get('first_name')
                post.last_name= request.POST.get('last_name')
                post.phone_number=request.POST.get('phone_number')
                post.email=request.POST.get('email')
                post.content=request.POST.get('content')
                post.save()
                
                return render(request, 'base.html')  

        else:
                post=Post()
                return render(request,'base.html')










    
    
