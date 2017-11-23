from django.shortcuts import render
from db_viewer.models import Users

user_current = 0

# Create your views here.
def index(request):
    return render(request,'db_viewer/index.html')

def games(request):
    return render(request,'db_viewer/games.html')

def game_id(request,appid):
    return render(request,'db_viewer/appid.html',{})

def users(request):
    global user_current
    if(request.GET.get('next')):
        user_current += 10
        entries = Users.objects.all()[user_current:user_current+10]
        return render(request,'db_viewer/users.html', {'users':entries})
    entries = Users.objects.all()[user_current:user_current+10]
    return render(request,'db_viewer/users.html',{'users':entries})