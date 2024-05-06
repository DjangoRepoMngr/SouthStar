from django.shortcuts import render
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect ,redirect)
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.urls import resolve, reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from client.forms import CreateIRouteForm, ClientForm
from .models import route, client
from django.db.models import Count, Q
from django.shortcuts import render

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
@user_passes_test(lambda u: u.is_superuser or u.groups.filter(name='supervisor').exists())
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

@login_required
@user_passes_test(lambda u: u.is_superuser or u.groups.filter(name='supervisor').exists())
@csrf_exempt
def route_list(request):

    list = route.objects.annotate(
        active_count=Count('client', filter=Q(client__client_status=1)),
        inactive_count=Count('client', filter=Q(client__client_status=0)),
        black_list_count=Count('client', filter=Q(client__is_black_list=True)),
        dishonest_count=Count('client', filter=Q(client__is_dishonest=True)),
        changed_location_count=Count('client', filter=Q(client__is_changed_location=True)),
        total_clients=Count('client')
    ).filter(status = 1)

    name_query = request.GET.get('name_query')

    if name_query != None:
        list = list.filter(name__contains = name_query)

    context = {
        'list': list,
    }

    return render(request, 'route_list.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser or u.groups.filter(name='supervisor').exists())
@csrf_exempt
def route_edit(request,id):

    obj = get_object_or_404(route,id = id)
    form = CreateIRouteForm(request.POST or None, instance= obj)

    context = {
        'form' : form ,
    }

    if request.method == "POST":
        if form.is_valid():
            obj = form.save()
            return redirect('client:route_list')

    return render(request, 'route_creator.html',context)


@login_required
@csrf_exempt
def client_creator(request):

    form = ClientForm(request.POST or None)

    context = {
        'form' : form ,
    }

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('client:route_list')

        else:
            # Add form errors to context
            context['form_errors'] = form.errors.as_ul()

    return render(request, 'client_creator.html',context)

@login_required
@csrf_exempt
def client_edit(request, id):

    obj = get_object_or_404(client, id = id)
    form = ClientForm(request.POST or None, instance= obj)

    context = {
        'form' : form ,
    }

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('client:route_list')

        else:
            # Add form errors to context
            context['form_errors'] = form.errors.as_ul()

    return render(request, 'client_creator.html',context)



@login_required
@csrf_exempt
def client_route_list(request,id):
    """ shows the clients in a specific route """
    client_list = client.objects.filter(route = id).filter(status = 1)
    this_route = route.objects.filter(id = id)
    context = {
        'clients' : client_list ,
        'route' : this_route[0],
    }

    return render(request, 'client_route_list.html',context)