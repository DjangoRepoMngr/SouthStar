from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = "client"

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path('login_timeout/', views.login_timeout, name='login_timeout'),

    # route
    path('route_creator/', views.route_creator, name='route_creator'),
    path('route_list/', views.route_list, name='route_list'),

]