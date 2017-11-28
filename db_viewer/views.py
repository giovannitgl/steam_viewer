from django.shortcuts import render,redirect,get_object_or_404
from db_viewer.models import User,Friendship,Userapps,App,Review,Relatedapps
from django.http import Http404

user_current = 0
games_current = 0

# Create your views here.
def index(request):
    if request.GET.get('games'):
        return redirect('games', permanent=True)
    elif request.GET.get('users'):
        return redirect('users', permanent=True)
    return render(request,'db_viewer/index3.html')

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
    elif(request.GET.get('prev')):
        if user_current > 10:
            disabled = ''
            user_current -= 10
        elif user_current == 10:
            user_current -= 10
    entries = User.objects.all()[user_current:user_current+10]
    return render(request,'db_viewer/users2.html',{'users':entries,'disabled':disabled})

def userid(request,steamid):
    if(request.GET.get('steamid')):
        return redirect(userid,request.GET.get('steamid'))
    elif(request.GET.get('appid')):
        return redirect(apps,request.GET.get('appid'))
    try:
        entry = get_object_or_404(User,pk=steamid)
    except User.DoesNotExist:
        raise Http404("No user with such id")
    friends = Friendship.objects.filter(uid1__uid=steamid)
    games = Userapps.objects.filter(uid=steamid)
    return render(request,'db_viewer/userid.html',{'user':entry,'friends':friends,'games':games})

def apps(request,appid):
    if(request.GET.get('appid')):
        return redirect(apps,request.GET.get('appid'))
    try:
        entry = get_object_or_404(App,pk=appid)
    except App.DoesNotExist:
        raise Http404("No game with such id")
    review = Review.objects.get(appid__appid=appid)
    related = Relatedapps.objects.filter(appid__appid=appid)
    return render(request,'db_viewer/appid.html',{'game':entry,'review':review,'pos':review.positive,'neg':review.total-review.positive,'related':related})

def games(request):
    if request.GET.get('appid'):
        return redirect(apps, request.GET.get('appid'))
    global games_current
    disabled = 'disabled'
    if request.GET.get('next'):
        games_current += 10
        disabled = ''
    elif request.GET.get('prev'):
        if games_current > 10:
            disabled = ''
            games_current -= 10
        elif games_current == 10:
            games_current -= 10
    entries = App.objects.all()[games_current:games_current+10]
    return render(request,'db_viewer/games2.html',{'games':entries})
