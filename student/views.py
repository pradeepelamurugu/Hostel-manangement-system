from django.shortcuts import render,redirect
from student.forms import *
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from student.models import *


# Create your views here.
def home(request):
    return render(request, 'student/base.html', {})

def register(request):
    return render(request,'student/register.html')

@login_required
def userLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def registerStudent(request):
    registered=False
    if request.method=='POST':
        var_studentForm=studentForm(request.POST)

        if var_studentForm.is_valid():
            studentprimary=var_studentForm.save()
            studentprimary.set_password(studentprimary.password)
            studentprimary.save()
            registered=True
            return redirect('userLogin')
    else:
        var_studentForm=studentForm()
    return render(request,'student/registerStudent.html',{'var_studentForm':var_studentForm,'registered':registered})

def userLogin(request):
    invalidlogin=False
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('student'))
            else:
                return HttpResponse('Account not active')
        else:
            invalidlogin=True
            return redirect('registerStudent')
    else:
        return render(request,'student/login.html',{'invalidlogin':invalidlogin})

def wardenLogin(request):
    invalidlogin=False
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('warden'))
            else:
                return HttpResponse('Account not active')
        else:
            invalidlogin=True
            return redirect('registerWarden')
    else:
        return render(request,'student/wardenlogin.html',{'invalidlogin':invalidlogin})

def student_detail(request):
    if request.method == "POST":
        form = detailform(request.POST)
        if form.is_valid():
            stu = form.save(commit=False)
            stu.name = request.user
            stu.save()
            return redirect('student')
    else:
        form = detailform()

    return render(request, 'student/studentdetail.html', {'form': form})

def warden_detail(request):
    if request.method == "POST":
        form = wardendetailform(request.POST)
        if form.is_valid():
            war = form.save(commit=False)
            war.name = request.user
            war.save()
            return redirect('warden')
    else:
        form = wardendetailform()

    return render(request, 'student/wardendetail.html', {'form': form})

def student(request):
    return render(request, 'student/student.html', {})

def warden(request):
    return render(request, 'student/warden.html', {})

def registerWarden(request):
    registered=False
    if request.method=='POST':
        var_wardenForm=wardenForm(request.POST)
        if var_wardenForm.is_valid():
            wardenprimary=var_wardenForm.save()
            wardenprimary.set_password(wardenprimary.password)
            wardenprimary.save()
            registered=True
    else:
        var_wardenForm=wardenForm()
    return render(request,'student/registerWarden.html',{'var_wardenForm':var_wardenForm,'registered':registered})


def status(request):
    room_list = Room.objects.all()

    context = {'rooms': room_list}
    return render(request, 'student/status.html', context)



@login_required
def createroom(request):
    if request.method == "POST":
        form = createroomform(request.POST)
        if form.is_valid():
            ro = form.save(commit=False)
            # ro.name = createroomform.name
            ro.save()
            return redirect('warden')
    else:
        form = createroomform()

    return render(request, 'student/createroom.html', {'form': form})

def feesstatus(request):
    stu_list = Student.objects.all()
    context = {'students': stu_list}
    return render(request, 'student/feesstatus.html', context)


def passapply(request):
    if request.method == "POST":
        form = passapplyform(request.POST)
        if form.is_valid():
            pas = form.save(commit=False)
            pas.applier = Student.student_name
            pas.save()
            return redirect('student')
    else:
        form = passapplyform()
    return render(request, 'student/passapply.html', {'form': form})

def passdecision(request):

    pass_list = Pass.objects.all()
    context = {'passes': pass_list}
    return render(request, 'student/passdecision.html', context)

# @login_required
# def dashboard(request):
#     try:
#         current=request.student.is_student
#     except Student.DoesNotExist:
#         current=request.student.is_student
#     if current.is_student:
#         return redirect('/student/')
#     else:
#         return redirect('/wardenDash/')
#     return render(request,'student/dashboard.html')
#
# def studentDash(request):
#     return render(request,'student/studentDash.html')
#
# def wardenDash(request):
#     return render(request,'student/wardenDash.html')
# def hostel_detail_view(request, hostel_name):
#     try:
#         this_hostel = Hostel.objects.get(name=hostel_name)
#     except Hostel.DoesNotExist:
#         raise Http404("Invalid Hostel Name")
#     context = {
#         'hostel': this_hostel,
#         'rooms': Room.objects.filter(
#             hostel=this_hostel)}
#     return render(request, 'hostels.html', context)
