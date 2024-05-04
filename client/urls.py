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
    path('route_edit/<int:id>', views.route_edit, name='route_edit'),

    #client
    path('client_creator/', views.client_creator, name='client_creator'),
    path('client_route/<int:id>', views.client_route_list, name='client_route'),
    path('client_edit/<int:id>', views.client_edit, name='client_edit'),

]