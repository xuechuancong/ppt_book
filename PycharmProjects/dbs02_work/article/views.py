from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django import forms
from article.models import User
import json

# Create your views here.
def hello(request):
    return HttpResponse('hello, world! django')

# def index(request):
#     return render(request, 'index.html')

#from django.contrib.auth import authenticate, login
def passwd():
    return HttpResponse('post')

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    if request.method == 'POST':
        # mas = request.method
        # return HttpResponse(mas)
        # print(request.POST['username'])
        # username = request.POST['username']
        # password = request.POST['password']
        json_receive = json.loads(request.body)
        return HttpResponse('OOO')
        # username = json_receive['/passwd']
        # password = json_receive['passwd']

        # user = authenticate(username=username, password=password)
        # if user is not None:
        #     if user.is_active:
        #         login(request, user)
        #         context = {'username': username, 'address': password}
        #         # return HttpResponse("hel")
        #         return render(request, 'index.html', {'dict': json.dump(context)})
        #         # Redirect to a success page.
        #     else:
        #         return HttpResponse("hello")
                # return render(request, 'index.html', {'error': '用户名'})
                # Return a 'disabled account' error message
        # else:
        #     return HttpResponse("pp")
            # return render(request, 'index.html', {'error': 'invalid login'})
            # Return an 'invalid login' error message.





