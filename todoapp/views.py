from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoListItem

def todolistView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'todolist.html',
    {'all_items':all_todo_items})

def addtodolistView(request):
    x = request.POST['content']
    new_item = TodoListItem(content = x).save()
    return HttpResponseRedirect('/todoapp/')

def deletetodolistView(request, pk):
    y = TodoListItem.objects.get(id= pk).delete()
    return HttpResponseRedirect('/todoapp/')