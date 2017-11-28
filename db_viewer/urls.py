from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^games/(?P<appid>\d+)/$',views.apps,name='appid'),
    url(r'^games/',views.games,name='games'),
    url(r'^users/(?P<steamid>\d+)/$',views.userid,name='userid'),
    url(r'^users/',views.users,name='users'),
]
