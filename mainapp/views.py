from django . shortcuts import render,redirect
import re
from django.contrib import messages
from django.contrib.auth.models import User
from mainapp import models
from mainapp.models import TODOO
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def signup(request): 
    def validate_password(pwd):
        errors = []
        if len(pwd) < 8:
            errors.append('Password must be at least 8 characters long.')
        if not re.search(r'[A-Z]', pwd):
            errors.append('Password must contain at least one uppercase letter.')
        if not re.search(r'[a-z]', pwd):
            errors.append('Password must contain at least one lowercase letter.')
        if not re.search(r'[0-9]', pwd):
            errors.append('Password must contain at least one digit.')
        if not re.search(r'[!@#$%^&*()_+\-=[\]{};:\'"\\|,.<>/?]', pwd):
            errors.append('Password must contain at least one special character.')
        return errors

    if request.method=='POST':
        frm=request.POST.get('frm')
        emailid = request.POST.get('email')
        pwd = request.POST.get('pwd')

        # Validate password server-side
        pwd_errors = validate_password(pwd or '')
        if pwd_errors:
            for e in pwd_errors:
                messages.error(request, e)
            return render(request, 'signup.html')

        # Check duplicates
        if User.objects.filter(username=frm).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'signup.html')
        if User.objects.filter(email=emailid).exists():
            messages.error(request, 'Email is already registered.')
            return render(request, 'signup.html')

        # Create user
        try:
            my_user = User.objects.create_user(frm, emailid, pwd)
            my_user.save()
            messages.success(request, 'Signup successful. Please login.')
            return redirect('/login')
        except Exception as exc:
            messages.error(request, 'Error creating account: ' + str(exc))
            return render(request, 'signup.html')

    return render(request,'signup.html')

def loginn(request):
    if request.method == 'POST':
        frm = request.POST.get('frm')
        pwd = request.POST.get('pwd')

        if not frm or not pwd:
            messages.error(request, 'Please enter both username and password.')
            return render(request, 'login.html', {'frm': frm or ''})

        userr = authenticate(request, username=frm, password=pwd)
        if userr is not None:
            login(request, userr)
            return redirect('/todopage')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login.html', {'frm': frm})

    return render(request, "login.html")

@login_required(login_url='/login')
def todo(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        print(title)
        obj=models.TODOO(title=title,user=request.user)
        obj.save()
        res=models.TODOO.objects.filter(user=request.user).order_by('date')
        return redirect('/todopage',{'res':res})
    res=models.TODOO.objects.filter(user=request.user).order_by('date')
    return render(request,'todo.html',{'res':res})

@login_required(login_url='/login')
def edit_todo(request,srno):
    if request.method == 'POST':
        title=request.POST.get('title')
        print(title)
        obj=models.TODOO.objects.get(srno=srno)
        obj.title=title
        obj.save()
        user=request.user
        return redirect('/todopage',{'obj':obj})
    obj=models.TODOO.objects.get(srno=srno)
    return render(request,'edit_todo.html',{'obj':obj})

@login_required(login_url='/login')
def delete_todo(request,srno):
    obj=models.TODOO.objects.get(srno=srno)
    obj.delete()
    return redirect('/todopage')

def signout(request):
    logout(request)
    return redirect('/login')