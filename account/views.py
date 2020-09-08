from django.shortcuts import render, redirect
from django.contrib import auth
from .models import User

# Create your views here.
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(email=request.POST['uemail'],password=request.POST['pass'])
        if user is not None:
            auth.login(request, user)
            if user.is_cuser:
                return redirect('home')
            else:
                return redirect('sin')
        else:
            try:
                user = User.objects.get(email=request.POST['uemail'])
                if user.is_active:
                    return render(request, 'account/login.html',{'error':'Incorrect Password'})
                else:
                    return render(request, 'account/login.html',{'error':'Account is deactivated'})
            except:
                return render(request, 'account/login.html',{'error':'Incorrect Email'})
    else:
        return render(request, 'home.html')