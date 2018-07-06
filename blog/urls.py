from django.conf.urls import url
from . import views

urlpatterns=[
    
    #main
    url(r'^main/$',views.main,name='main'),
    
    #guest book
    url(r'^$',views.post_list,name='post_list'),
    url(r'^post/(?P<pk>\d+)/$',views.post_detail,name='post_detail'),
    url(r'^post/new/&',views.post_new,name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$',views.post_edit,name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    
    #board
    url(r'^board/$',views.post_board_list,name='post_board_list'),
    url(r'^post/(?P<pk>\d+)/board/$',views.post_board_detail,name='post_board_detail'),
    url(r'^post/board/new/&',views.post_board_new,name='post_board_new'),
    url(r'^post/(?P<pk>\d+)/board/edit/$',views.post_board_edit,name='post_board_edit'),
    url(r'^post/(?P<pk>\d+)/board/remove/$', views.post_board_remove, name='post_board_remove'),
    
    ]