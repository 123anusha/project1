from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import User


def c_signup(request):
    if request.method == 'POST':
        if request.POST['pass1'] == request.POST['pass2']:
            try:
                user = User.objects.get(email=request.POST['uemail'])
                return render(request, 'account/cregistration.html',{'error':'Email already exist'})
            except User.DoesNotExist:
                user = User.objects.create_customer(email=request.POST['uemail'],password=request.POST['pass1'])
                cp.fname = request.POST['fnam']
                cp.lname = request.POST['lnam']
                if request.POST['mnam']!='':
                    cp.mname = request.POST['mnam']
                cp.address = request.POST['addr']
                cp.phone_no = request.POST['phone']
                cp.vuser = user
                try:
                    cp.save()
                    return redirect('sin')
                except:
                    user.delete()
                    return render(request,'account/cregistration.html',{'error':'Fill up the form correctly'})
        else:
            return render(request, 'account/cregistration.html',{'error':'Password did not match'})
    else:
        return render(request, 'account/cregistration.html')



def login(request):
    if request.method == 'POST':
        user = auth.authenticate(email=request.POST['uemail'],password=request.POST['pass'])
        if user is not None:
            auth.login(request, user)
            if user.is_cuser:
                return redirect('chome')
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
        return render(request, 'account/login.html')

@login_required(login_url='sin')
def logout(request):
    auth.logout(request)
    return redirect('sin')
