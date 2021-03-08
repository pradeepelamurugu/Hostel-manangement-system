from django.shortcuts import render,redirect
from student.forms import *
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from student.models import *
from HostelManagementSystem.settings import EMAIL_HOST_USER
from django.db import transaction
from django.core.mail import send_mail
from django.contrib.admin.views.decorators import staff_member_required,user_passes_test



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
            # return redirect('userLogin')
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
            return redirect('home')
    else:
        return render(request,'student/wardenlogin.html',{'invalidlogin':invalidlogin})

@login_required
def student_detail(request):
    if request.method == "POST":
        form = detailform(request.POST)
        if form.is_valid():
            stu = form.save(commit=False)
            stu.name = request.user
            stu.save()
            return redirect('student')
    else:
        stu = Student.objects.filter(student_name=request.user).first()
        form = detailform(instance=stu)
        return render(request, "student/studentdetail.html", {'form': form})

    return render(request, 'student/studentdetail.html', {'form': form})

# @transaction.atomic
# def student_detail(request):
#     if request.method == "POST":
#         form = detailform(request.POST)
#         if form.is_valid():
#             stu = form.save(commit=False)
#             stu.name = request.user
#             stu.save()
#             return redirect('student')
#     else:
#         form = detailform()
#
#     return render(request, 'student/studentdetail.html', {'form': form})

# def warden_detail(request):
#     if request.method == "POST":
#         form = wardendetailform(request.POST)
#         if form.is_valid():
#             war = form.save(commit=False)
#             war.name = request.user
#             war.save()
#             return redirect('warden')
#     else:
#         form = wardendetailform()
#
#     return render(request, 'student/wardendetail.html', {'form': form})
@login_required
@staff_member_required
def warden_detail(request):
    if request.method == "POST":
        form = wardendetailform(request.POST)
        if form.is_valid():
            war = form.save(commit=False)
            war.name = request.user
            war.save()
            return redirect('warden')
    else:
        war = Warden.objects.filter(name=request.user).first()
        form = wardendetailform(instance=war)
        return render(request, "student/wardendetail.html", {'form': form})

    return render(request, 'student/wardendetail.html', {'form': form})

@login_required
def student(request):
    stu = Student.objects.filter(student_name = request.user).first()
    context = {'stude': stu}
    return render(request, 'student/student.html',context)

@login_required
@staff_member_required
def warden(request):
    war = Warden.objects.filter(name=request.user).first()
    context = {'ward': war}
    return render(request, 'student/warden.html', context)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def mentor(request):
    students = Student.objects.all()
    feepaid = Student.objects.filter(fees = True)
    feenot = Student.objects.filter(fees = False)
    pasapl = Pass.objects.all()
    roomalloted = Student.objects.filter(room_allotted = True)
    roomnotalloted = Student.objects.filter(room_allotted = False)
    # passapproved = Pass.objects.filter(status=)
    passnotapproved = Pass.objects.filter(status=None)
    roomtotal = Room.objects.all()
    s = 0
    fp = 0
    fn = 0
    pa = 0
    ra = 0
    rn = 0
    pas = 0
    pasn = 0
    rom = 0
    for i in students:
        s = s + 1
    for i in feepaid:
        fp = fp + 1
    for i in feenot:
        fn = fn + 1
    for i in pasapl:
        pa = pa + 1
    for i in roomalloted:
        ra = ra + 1
    for i in roomnotalloted:

        rn = rn + 1

    # for i in passapproved:
    #     pas = pas+1
    for i in passnotapproved:
        pasn = pasn+1
    for i in roomtotal:
        rom = rom+1

    if (rn == 0):
        rn = rom-s
    pas = pa - pasn
    d1 = {'s': s, 'fp': fp, 'fn': fn, 'pa': pa,'ra':ra, 'rn':rn,'pas':pas,'pasn':pasn,'rom':rom}
    return render(request, 'student/mentor.html',d1)


@login_required
@staff_member_required
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
@staff_member_required
def createroom(request):
    if request.method == "POST":
        form = createroomform(request.POST)
        if form.is_valid():
            ro = form.save(commit=False)
            ro.save()
            return redirect('warden')
    else:
        form = createroomform()

    return render(request, 'student/createroom.html', {'form': form})

@login_required
@staff_member_required
def feesstatus(request):
    stu_list = Student.objects.all()
    context = {'students': stu_list}
    return render(request, 'student/feesstatus.html', context)

@login_required
def passapply(request):
    if request.method == "POST":
        form = passapplyform(request.POST)
        if form.is_valid():
            pas = form.save(commit=False)
            pas.applier = request.user
            pas.save()
            return redirect('student')
    else:
        form = passapplyform()
    return render(request, 'student/passapply.html', {'form': form})

@login_required
@staff_member_required
def passdecision(request):

    pass_list = Pass.objects.all()
    context = {'passes': pass_list}
    return render(request, 'student/passdecision.html', context)

@login_required
@staff_member_required
def sendmail(request):
    pas = Pass.objects.filter(applier=request.POST["appliername"]).first()
    use = User.objects.filter(username=request.POST["appliername"]).first()
    if request.method == 'POST':
        if 'accept' in request.POST["decision"]:
            pas.status = 'accpeted'
            pas.save()
        mai = use.email
        subject = 'Pass approval'
        message = 'Hello, '+use.username+'\nYour pass was approved!!!\nThat is from '+str(pas.fromdt)+'to '+str(pas.todt)+'.\nThank you \nregards\n-'+request.user.email+'.'
        recepient = mai
        send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently = False)

        return render(request, 'student/mailsent.html', {'recepient': recepient})
    return render(request, 'student/passdecision.html')

@user_passes_test(lambda u: u.is_superuser)
def students_list(request):
    stu = Student.objects.all()
    context = {'students':stu}
    return render(request, 'student/students_list.html', context)

@user_passes_test(lambda u: u.is_superuser)
def warden_list(request):
    war = Warden.objects.all()
    context = {'ward':war}
    return render(request, 'student/warden_list.html', context)

@user_passes_test(lambda u: u.is_superuser)
def hostel_list(request):
    host = Hostel.objects.all()
    context = {'hostels':host}
    return render(request, 'student/hostel_list.html', context)

@user_passes_test(lambda u: u.is_superuser)
def pass_list(request):
    pas = Pass.objects.all()
    context = {'passes':pas}
    return render(request, 'student/pass_list.html', context)

# @user_passes_test(lambda u: u.is_superuser)
def hostel_detail_view(request, hostel_name):
    try:
        this_hostel = Hostel.objects.get(name=hostel_name)
    except Hostel.DoesNotExist:
        raise Http404("Invalid Hostel Name")
    context = {
        'hostel': this_hostel,
        'rooms': Room.objects.filter(
            hostel=this_hostel)
    }
    return render(request, 'student/hostel_detail_view.html', context)


def about(request):
    return render(request, 'student/about.html')

def mentorLogin(request):
    invalidlogin=False
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('mentor'))
            else:
                return HttpResponse('Account not active')
        else:
            invalidlogin=True
            return redirect('home')
    else:
        return render(request,'student/mentorlogin.html',{'invalidlogin':invalidlogin})

def hostel_detail_list(request):
    host = Hostel.objects.all()
    context = {'hos': host}
    return render(request, 'student/hostel_detail_list.html',context)

@transaction.atomic
def selectroom(request):
    if request.method=='POST':
        form = selectroomform(request.POST)
        if form.is_valid():
            stu = Student.objects.filter(student_name = request.user).first()
            rom = Room.objects.filter(name = form.cleaned_data.get("room")).first()
            stu.room = rom
            stu.room_allotted = True
            stu.save()
            return redirect('student')
    else:
        form = selectroomform()
    return render(request, 'student/selectroom.html', {'form': form})




















        # def passapply(request):
            # if request.method == "POST":
            #     form = passapplyform(request.POST)
            #     if form.is_valid():
            #         pas = form.save(commit=False)
            #         pas.applier = request.user
            #         pas.save()
            #         return redirect('student')
            # else:
            #     form = passapplyform()
            # return render(request, 'student/passapply.html', {'form': form})
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
