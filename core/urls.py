from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('signup', views.signup, name='signup'),
    path('follow', views.follow, name='follow'),
    path('signin', views.signin, name='signin'),
    path('search', views.search, name='search'),
    path('profile/<str:pk>', views.profile, name='upload'),
    path('like-post', views.like_post, name='like_post'),
    path('logout', views.logout, name='logout'),
    path('upload', views.upload, name='upload'),
]