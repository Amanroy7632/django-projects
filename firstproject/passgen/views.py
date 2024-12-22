from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import random
# Create your views here.
def home(request):
    return render(request,"home.html")
    # return HttpResponse("<h1>Hello World!</h1> <br> <p>Welcome to the django project.</p>")
def passgen(request):
    # print(request)

    char = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    passLength =int( request.GET.get("length")) 
    password=""
    for i in range(passLength):
        password +=random.choice(char)
    responseData = {
        "success":True,
        "password":password
    }
    # return JsonResponse(responseData)
    return render(request,"passgen.html",responseData)
