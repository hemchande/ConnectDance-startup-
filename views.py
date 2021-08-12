from django. shortcuts import render,redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from .forms import *


def home(request):
   if request.user.is_authenticated:
       students = Students.objects.filter(Teacher_name = request.user.username)
       context ={
           'students': Students,
       }
       return render(request, 'hr.html',context)
   else:
       teacher = Teacher.objects.all()
       context= {
           'teacher' = teacher,

       }
       return render(request, 'TeacherApply.html', context)

def logoutUser(request):
   logout(request)
   return redirect('login')

def loginUser(request):
   if request.user.is_authenticated:
       return redirect('home')
   else:
       if request.method =="POST":
           name = request.POST.get('username')
           password = request.POST.get('password')
           user = authenticate(request,username = name, password = password)

       if user is not None:
           login(request,user)
           return redirect('home')
       return render(request,'login.html')

def registerUser(request):
   if request.user.is_authenticated:
       return redirect('home')
   else:
       Form = UserCreationForm()
       if request.method == 'POST':
           Form = UserCreationForm(request.POST)

           if Form.is_valid():
               currUser = Form.save()
               Teacher.objects.create( user = currUser, name = currUser.username)
               return redirect('login')

def applyPage(request):
   form = ApplyForm()
   if request.method =='POST':
       form = ApplyForm(request.POST, request.FILES)

       if form.is_valid():
           form.save()
