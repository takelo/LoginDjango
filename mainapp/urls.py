# from django.conf.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^registro/', views.register_page, name="registro"),
    url('^inicio/', views.index, name="inicio"),
    url('^login/', views.login_page, name="login"),
    url('^logout/', views.logout_user, name="logout"),
]