from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden
from .forms import UserForm
from .models import user

# Create your views here.

def hello(request):
    return HttpResponse("Hello world!")

def users_list(request):
    users = user.objects.all()
    return render(request, 'newapp/users_list.html',{'users':users})

# def new_user(request):
#     print("Request==>", request)
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('users_list')
#     else:
#         form = UserForm()
#     return render(request, 'newapp/new_user.html', {'form': form})

def new_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            role = form.cleaned_data['role']

            # Check if a user with the same properties already exists
            if user.objects.filter(name=name, email=email, role=role).exists():
                error_message = "User with the same properties already exists."
                return render(request, 'newapp/new_user.html', {'form': form, 'error_message': error_message})
            else:
                form.save()
                return redirect('users_list')
    else:
        form = UserForm()
    return render(request, 'newapp/new_user.html', {'form': form})

def user_details(request, user_id):
    try:
        userDetail = get_object_or_404(user, pk=user_id)
        return render(request, 'newapp/user_details.html', {'user': userDetail})
    except user.DoesNotExist:
        return HttpResponseNotFound("User not found")

def delete_user(request, user_id):
    if request.method == "POST":
        userDetail = get_object_or_404(user, pk=user_id)
        userDetail.delete()
        return redirect('users_list')
    else:
        return HttpResponseForbidden("Forbidden")