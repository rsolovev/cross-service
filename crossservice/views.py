# dappx/views.py
from django.contrib import auth
from django.shortcuts import render, redirect
from crossservice.forms import UserForm, UserProfileInfoForm, EditProfileForm, PostServiceForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from crossservice.models import *
from django.views.generic import ListView, DetailView

# start page - just render html page
from crse import secret_keys


def index(request):
    return render(request, 'index.html')


# success login response
@login_required
def special(request):
    return HttpResponse("You are logged in !")


# redirecting to index page after logging out
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def user_delete(request):
    user = auth.get_user(request)
    user.set_password(secret_keys.passwd)
    user.is_active = False
    user.save()
    auth.logout(request)
    return render(request, 'login.html')


# registration algorithm
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'registration.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


# login logic
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})


# user dashboard render
@login_required()
def dashboard(request):
    user = auth.get_user(request)
    username = user.get_username()
    info = UserProfileInfo.objects.filter(user_id=user.id)
    return render(request, 'dashboard.html', {'username': username, 'info': info})


"""
Update User's additional info (not uname or password)
Works on django update forms
"""
def user_update(request):
    user = auth.get_user(request)
    if request.method == 'POST':
        form = EditProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            UserProfileInfo.objects.filter(user_id=user.id).update(bio=str(form.cleaned_data['bio']))
            UserProfileInfo.objects.filter(user_id=user.id).update(location=str(form.cleaned_data['location']))
            UserProfileInfo.objects.filter(user_id=user.id).update(organization=str(form.cleaned_data['organization']))

            return redirect('crossservice:dashboard')
    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'update.html', {'form': form})


"""
Post a service, service is assigned to particular user as 'owner'
Works on django POST forms
After user posting, instance is added to db 
"""
def post_service(request):
    if request.method == 'POST':
        user = auth.get_user(request)
        newPost = ServicePostInfo()
        form = PostServiceForm(data=request.POST, instance=newPost)
        if form.is_valid():
            form.save()
            newPost.user_id = user.id
            form.save()
            return redirect('crossservice:dashboard')
    else:
        form = PostServiceForm()
    return render(request, 'post_service.html', {'form': form})


class listPosts(ListView):
    model = ServicePostInfo


class detailPosts(DetailView):
    context_object_name = 'post'
    queryset = ServicePostInfo.objects.all()
