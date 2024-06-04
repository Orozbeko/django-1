from django.shortcuts import render
from django.http import HttpResponse
from random import randint

def about_me_view(request):
    if request.method == 'GET':
        return HttpResponse("Меня зовут [Орозбеков Мурас], мне [17] лет.")


def hobby_view(request):
    if request.method == 'GET':
        return HttpResponse('Любимое хобби это играть футбол.')
    

def time_view(request):
    if request.method == 'GET':
        return HttpResponse(f"{datetime.datetime.now()}")
    

def random_numbers_view(request):
    if request.method == 'GET':
        return HttpResponse(random.randint(1, 100))
