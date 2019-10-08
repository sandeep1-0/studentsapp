from django.shortcuts import render, redirect
from django.http import *
from django.contrib.auth import login as UserLogin, logout as UserLogout, authenticate
from .forms import *
from .models import *


def Registration(request):
    form = RegForm()
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            user = User()
            user.username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password1'])
            user.save()
            request.session['username'] = form.cleaned_data['username']
            print("once more")
            return HttpResponseRedirect('detailform')
    context = {'form': form}
    return render(request, 'registration.html', context)


def detailform(request):
    form1 = fulldetails()
    username = request.session.get('username')
    if request.method == 'POST':
        form1 = fulldetails(request.POST, request.FILES)
        if form1.is_valid():
            data = details.objects.create(username=User.objects.get(username=username),
                                          firstname=form1.cleaned_data['firstname'],
                                          lastname=form1.cleaned_data['lastname'],
                                          student_dpt=form1.cleaned_data['student_dpt'],
                                          student_img=request.FILES['student_img'])
            del request.session['username']
        return redirect(Login)
    return render(request, 'detailform.html', {'form1': form1})


def Login(request):
    if request.user.username:
        return redirect(dashboard)
    message = ''
    form2 = LoginForm
    if request.method == 'POST':
        form2 = LoginForm(request.POST)
        if form2.is_valid():
            username = form2.cleaned_data['username']
            password = form2.cleaned_data['password']
            user = authenticate(username=username, password=password)
            try:
                student = details.objects.filter(username=User.objects.get(username=user))
            except:
                student = None
            if student is None:
                message = 'Invalid login details!'
            else:
                return render(request, 'dashboard.html', {'student': student})
    return render(request, 'login.html', {'form2': form2, 'message': message})


def dashboard(request):
    return render(request, 'dashboard.html')


def logout(request):
    UserLogout(request)
    return redirect(Login)


def update(request):
    print(request.user.username)
    user = request.GET['username']
    data = details.objects.filter(username=User.objects.get(username=user)).first()
    form3 = fulldetails(instance=data)
    if request.method == 'POST':
        data.firstname = request.POST['firstname']
        data.lastname = request.POST['lastname']
        data.student_dpt = request.POST['student_dpt']
        if request.FILES.get('student_img'):
            data.student_img = request.FILES.get('student_img')
        data.save()
        return render(request, 'dashboard.html', {'data': data})
    return render(request, 'update.html', {'form3': form3})


def delete(request):
    user = request.GET['username']
    data = details.objects.get(username=User.objects.get(username=user))
    data1 = User.objects.get(username = user)
    data.delete()
    data1.delete()
    return redirect(viewall)
def viewall(request):
    students = details.objects.all()
    return render(request,'viewall.html',{'students':students})