from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

#registers new user and checks whether he/she as a company employee
def register_page (request):
    error = False
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            if email[len(email)-11::1] == 'alivaria.by':
                form.save()
                messages.success(request, request.POST.get('last_name') + ' ' + request.POST.get('first_name') + ', your account was successfully created')
                return redirect('identif:login')
            else:
                error = "Not an employee"
    else:
        form = CreateUserForm()
    context = {'form': form, 'error':error}
    return render (request, 'identif/reg.html', context)

#logs user in if input data's correct
def login_page (request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('actions:promos')
        else:
            messages.warning(request, 'Username or password is incorrect')
    return render (request, 'identif/login.html')

#logs user out
def logout_page (request):
    logout(request)
    return redirect('identif:login')
