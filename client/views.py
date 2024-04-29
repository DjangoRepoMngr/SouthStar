from django.shortcuts import render
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect ,redirect)
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.urls import resolve, reverse
from django.contrib.auth.decorators import login_required



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


    context = {

        'institute_center_list' : 1 ,
        'institute_count':1,
        'course_count':1,
        'student_count':1,
        'exam_count':1,
    }

    return render(request, 'Home.html',context)