from django.urls import path
from student import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/',views.register,name='register'),
    path('registerStudent/', views.registerStudent, name='registerStudent'),
    path('logout/', views.userLogout, name='logout'),
    path('login_student/',views.userLogin,name='userLogin'),
    path('login_warden/',views.wardenLogin,name='wardenLogin'),
    path('student/',views.student,name='student'),
    path('warden/',views.warden,name='warden'),
    path('details/', views.student_detail, name='detail'),
    path('wardendetails/', views.warden_detail, name='wardendetail'),
    path('registerWarden/',views.registerWarden,name='registerWarden'),
    # path('hostels/<slug:hostel_name>/', views.hostel_detail_view, name='hostel'),
    path('status/',views.status,name='status'),
    path('createroom/',views.createroom,name='createroom'),
    # path('dashboard', views.dashboard, name='dashboard'),
    path('feesstatus/',views.feesstatus,name='feesstatus'),
    path('passapply/',views.passapply,name='passapply'),
    path('passdecision/',views.passdecision,name='passdecision'),


]