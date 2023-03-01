from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login, logout
from .models import *


def index(request):
    return render(request,'index.html')

def login(request):
    error=""
    if request.method=='POST':
        u = request.POST['uname']
        p = request.POST['pswd']
        user = auth.authenticate(username=u,password=p)
        try:
            if user.is_staff:
                auth.login(request,user)
                error="no"
            elif user is not None:
                auth.login(request, user)
                error = "not"
            else:
                error="yes"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'login.html',d)

def contact_us(request):
    return render(request,'contact_us.html')

def admin_home(request):
    return render(request,'admin_home.html')

def add_room(request):
    error=""
    if request.method=='POST':
        rno = request.POST['roomno']
        p = request.POST['price']
        t = request.POST['rtype']
        s = request.POST['status']
        i = request.FILES['image']
        try:
            Room.objects.create(room_no=rno,image=i,type=t,price=p,status=s)
            error="no"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'add_room.html',d)


def signup(request):
    error=""
    if request.method=='POST':
        f = request.POST['fname']
        l = request.POST['lname']
        e = request.POST['email']
        c = request.POST['contact']
        dob = request.POST['dob']
        p = request.POST['pwd']
        g = request.POST['gender']
        i = request.FILES['profile_pic']
        try:
            user = User.objects.create_user(first_name=f,last_name=l,username=e,
                                            password=p)
            Signup.objects.create(user=user,mobile=c,image=i,gender=g,dob=dob)
            error="no"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'signup.html',d)


def logout(request):
    auth.logout(request)
    return redirect('/')

def user_home(request):
    return render(request,'user_home.html')

def feedback(request):
    error=""
    user = request.user
    data = Signup.objects.get(user=user)
    if request.method=="POST":
        n = request.POST['fname']
        e = request.POST['femail']
        c = request.POST['fphone']
        f = request.POST['fcomment']
        try:
            Feedback.objects.create(fname=n,femail=e,fcontact=c,feedback=f)
            error="no"
        except:
            error="yes"
    d = {'error':error,'data':data}
    return render(request,'feedback.html',d)

def view_feedback(request):
    data = Feedback.objects.all()
    d = {'data':data}
    return render(request,'view_feedback.html',d)

def delete_feedback(request,id):
    data = Feedback.objects.get(id=id)
    data.delete()
    return redirect('view_feedback')


def view_room_admin(request):
    data = Room.objects.all()
    d = {'data':data}
    return render(request,'view_room_admin.html',d)

def delete_room(request,id):
    data = Room.objects.get(id=id)
    data.delete()
    return redirect('view_room_admin')


def edit_room(request,id):
    error=""
    data = Room.objects.get(id=id)
    if  request.method=='POST':
        r = request.POST['roomno']
        p = request.POST['price']
        t = request.POST['rtype']
        s = request.POST['status']
        data.room_no=r
        data.price=p
        data.type=t
        data.status=s
        try:
            i = request.FILES['room_img']
            data.image=i
        except:
            pass
        try:
            data.save()
            error="no"
        except:
            error="yes"
    d = {'data':data,'error':error}
    return render(request,'edit_room.html',d)


def view_booking_admin(request):
    data = Booking.objects.all()
    d = {'data':data}
    return render(request,'view_booking_admin.html',d)


def view_user(request):
    data = Signup.objects.all()
    d = {'data':data}
    return render(request,'view_user.html',d)

def delete_user(request,id):
    data = User.objects.get(id=id)
    data.delete()
    return redirect('view_user')

def change_password_admin(request):
    error=""
    if request.method=='POST':
        c=request.POST['currentpassword']
        n=request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"
    d={'error':error}
    return render(request,'change_password_admin.html',d)

def edit_user(request):
    error=""
    data = request.user
    data2 = Signup.objects.get(user=request.user)
    if request.method=='POST':
        f = request.POST['fname']
        l = request.POST['lname']
        c = request.POST['contact']
        g = request.POST['gender']
        dob = request.POST['dob']
        data.first_name=f
        data.last_name=l
        data2.mobile=c
        data2.gender=g
        data2.dob=dob
        try:
            i = request.FILES['image']
            data2.image=i
        except:
            pass
        try:
            data.save()
            data2.save()
            error="no"
        except:
            error="yes"
    d = {'data':data,'data2':data2,'error':error}
    return render(request,'edit_user.html',d)

def view_room_user(request):
    data = Room.objects.all()
    d = {'data':data}
    return render(request,'view_room_user.html',d)


def book_room(request,id):
    error=""
    data2 = Signup.objects.get(user=request.user)
    data = Room.objects.get(id=id)
    if request.method=='POST':
        f = request.POST['fname']
        l = request.POST['lname']
        f = f + " " + l
        e = request.POST['email']
        rno = request.POST['roomno']
        c1 = request.POST['contact']
        c2 = request.POST['contact2']
        bd = request.POST['booking_date']
        td = request.POST['select_days']
        g = request.POST['gender']
        p = request.POST['price']
        p = int(p)*int(td)
        dob = request.POST['dob']
        try:
            Booking.objects.create(room_no=rno,fullname=f,email=e,contact1=c1,
                                   contact2=c2,booking_date=bd,days=td,gender=g,
                                   price=p,dob=dob,status="Pending")
            error="no"
        except:
            error="yes"
    d = {'data2':data2,'data':data,'error':error}
    return render(request,'book_room.html',d)

def my_booking(request):
    data = Booking.objects.all()
    d = {'data':data}
    return render(request,'my_booking.html',d)

def cancel_booking(requset,id):
    data = Booking.objects.get(id=id)
    data.delete()
    return redirect('my_booking')

def change_password_user(request):
    error=""
    if request.method=='POST':
        c=request.POST['currentpassword']
        n=request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"
    d={'error':error}
    return render(request,'change_password_user.html',d)

def delete_booking_admin(request,id):
    data = Booking.objects.get(id=id)
    data.delete()
    return redirect('view_booking_admin')


def change_status(request,id):
    error = ""
    data = Booking.objects.get(id=id)
    if request.method=='POST':
        s = request.POST['rstatus']
        data.status=s
        try:
            data.save()
            error="no"
        except:
            error="yes"
    d = {'data':data,'error':error}
    return render(request,'change_status.html',d)

def search(request):
    n = request.POST['name']
    data = Booking.objects.filter(email__icontains=n)
    d = {'data':data}
    return render(request,'view_booking_admin.html',d)
