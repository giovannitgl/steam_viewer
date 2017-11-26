from django.shortcuts import render,redirect,get_object_or_404
from db_viewer.models import Users,Friends,UserGames
from django.http import Http404

user_current = 0

# Create your views here.
def index(request):
    if(request.GET.get('games')):
        return redirect('games',permanent=True)
    elif(request.GET.get('users')):
        return redirect('users',permanent=True)
    return render(request,'db_viewer/index.html')

def games(request):
    return render(request,'db_viewer/games.html')

def game_id(request,appid):
    return render(request,'db_viewer/appid.html',{})

def users(request):
    if(request.GET.get('steamid')):
        return redirect(userid,request.GET.get('steamid'))
    global user_current
    disabled = 'disabled'
    if(request.GET.get('next')):
        user_current += 10
        disabled = ''
        # entries = Users.objects.all()[user_current:user_current+10]
        # return render(request,'db_viewer/users.html', {'users':entries})
    elif(request.GET.get('prev')):
        if user_current > 10:
            disabled = ''
            user_current -= 10
        elif user_current == 10:
            user_current -= 10
    entries = Users.objects.all()[user_current:user_current+10]
    return render(request,'db_viewer/users.html',{'users':entries,'disabled':disabled})

def userid(request,steamid):
    try:
        entry = get_object_or_404(Users,pk=steamid)
    except Users.DoesNotExist:
        raise Http404("No user with such id")
    friends = Friends.objects.filter(steamid1=steamid)
    games = UserGames.objects.filter(steamid=steamid)
    return render(request,'db_viewer/userid.html',{'user':entry,'friends':friends,'games':games})