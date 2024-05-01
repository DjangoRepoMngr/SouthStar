from django.shortcuts import render
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect ,redirect)
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.urls import resolve, reverse
from django.contrib.auth.decorators import login_required

from client.forms import CreateIRouteForm



@csrf_exempt
def login_view(request):

    next_url = request.GET.get('next')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                redirect_url = next_url if next_url else reverse('client:home')
                return HttpResponseRedirect(redirect_url)
            else:
                messages.error(request, 'نام کاربری یا گذرواژه اشتباه است ')
                return redirect('client:login')
        except ValueError as e:
            return redirect('client:login_timeout')
    else:
        # Render the login form
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('client:login'))

def login_timeout(request):

    error_message ='به دلیل خطا های متعدد 5 دقیقه ی دیگر تلاش کنید'

    return render(request, 'login_timeout.html', {'error_message': error_message})



@login_required
def home(request):

    return render(request, 'Home.html')

@login_required
@csrf_exempt
def route_creator(request):

    form = CreateIRouteForm(request.POST or None)

    context = {
        'form' : form ,
    }

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('client:route_list')

    return render(request, 'route_creator.html',context)