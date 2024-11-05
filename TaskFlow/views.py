from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

# Create your views here.
def home(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            #messages.success(request, "Login Successful!")
            return redirect('home')
        else:
            #messages.error(request, "Login Error")
            return redirect('home')
    else:
        return render(request, 'home.html', {})