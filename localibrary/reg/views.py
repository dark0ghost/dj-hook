from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth



def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        
        auth.login(request, user)

        return HttpResponseRedirect("/account/loggedin/")
    else:
        # Отображение страницы с ошибкой
        return HttpResponseRedirect("/account/invalid/")

def logout(request):
    auth.logout(request)

    return HttpResponseRedirect("/account/loggedout/")