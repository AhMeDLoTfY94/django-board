from django.shortcuts import render
from .models import Board

def home(request):
    boards=Board.objects.all()
    context={
        'boards':boards,
    }

    return render(request,"core/home.html",context)


def topics(request,board):
    board=Board.objects.get(id=board)

    context={
        "board":board,
    }

    return render(request,'core/topics.html',context)

def new_topic(request,board):
    board=Board.objects.get(id=board)

    context={
        "board":board,
    }



    return render(request,"core/new_topic.html",context)