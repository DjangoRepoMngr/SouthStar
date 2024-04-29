from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = "client"

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path('login_timeout/', views.login_timeout, name='login_timeout'),
    # path('edit_profile/<int:id>', views.edit_profile, name='edit_profile'),
    # path('delete_err/', views.delete_err, name='delete_err'),

]