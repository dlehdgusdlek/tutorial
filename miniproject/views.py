from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

from .models import Board_title, League,Player, Comment
def league(request):
    league = League.objects.all()
    result = ''
    for i in league:
        result+=i.l_name+'<br>'
    return HttpResponse(result)
    return render(
        request,'miniproject/league.html',
        {'data' : league}
        )

def player(request):
    player = Player.objects.all()
    result = ''
    for i in player:
        result+=i.name+'<br>'
    return HttpResponse(result)

# def comment(request):
#     id = request.GET.get('id')
    
#     comment = Comment.objects.filter(u_id__contains = id)
#     # result = ''
#     # for i in comment:
#     #     result+=i.comment+'<br>'
#     return render(
#         request,'miniproject/comment.html',
#         {'data' : comment}
#     )
#     return HttpResponse(comment)


def comment(request):
    id = request.GET.get('id')

    comment = Comment.objects.filter(u_id__contains = id)
    title = Board_title.objects.filter(u_id__contains = id)
    # result = ''
    # for i in comment:
    #     result+=i.comment+'<br>'
    return render(
        request,'miniproject/comment.html',
        {'comment' : comment, 'title' : title,}
    )
    return HttpResponse(comment)


