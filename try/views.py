from django.shortcuts import render, redirect, HttpResponse
from .models import *
# Create your views here.


def index(request):
    messages = list(Message.objects.all())
    messages.reverse()
    content = {
        'messages': messages
    }
    return render(request, 'index.html', content)


def create_link(request):
    text = request.POST['text']
    print(request.POST)
    new_mess = Message(text=text)
    new_mess.save()
    return redirect('/')


def file(request):
    if request.POST:
        print(request.POST)
        return HttpResponse('OK')
    else:
        return render(request, 'file.html', {})