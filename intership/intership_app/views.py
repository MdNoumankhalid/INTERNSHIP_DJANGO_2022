from django.shortcuts import render, redirect
from django.urls import reverse
from intership_app.models import UserRegistration,AddPayment, UserLogin, AddProduct, AddCategory, OtpCode,MyOrder

from django.core.files.storage import FileSystemStorage
import os
from intership.settings import BASE_DIR
import random
import smtplib
import datetime


def index(request):
    return render(request, 'index.html')


def reg(request):
    if request.method == 'POST':
        name = request.POST.get('t1')
        gender = request.POST.get('r1')
        city = request.POST.get('t2')
        address = request.POST.get('t3')
        pincode = request.POST.get('t4')
        contact = request.POST.get('t5')
        email = request.POST.get('t6')
        password = request.POST.get('t7')
        ucount = UserRegistration.objects.filter(email=email).count()
        if ucount >= 1:
            return render(request, 'reg.html', {'msg': 'This user is already exist'})
        else:
            UserRegistration.objects.create(name=name, gender=gender, city=city, address=address, pincode=pincode,
                                            contact=contact, email=email, password=password)
            UserLogin.objects.create(username=email, password=password, utype='user')
            return render(request, 'reg.html', {'msg': 'Thank you for registration'})
    return render(request, 'reg.html')


def reg_view(request):
    userdata = UserRegistration.objects.all()
    return render(request, 'reg_view.html', {'userdata': userdata})


def login(request):
    if request.method == "POST":
        username = request.POST.get('t1')
        password = request.POST.get('t2')
        request.session['username']=username
        ucount = UserLogin.objects.filter(username=username).count()
        if ucount >= 1:
            udata = UserLogin.objects.get(username=username)
            upass = udata.password
            utype = udata.utype
            if password == upass:
                if utype == "user":
                    udict=AddCategory.objects.values('cat_name').distinct()
                    return render(request, 'user_home.html',{'udict':udict})
                if utype == "admin":
                    return render(request, 'admin_home.html')
                else:
                    return render(request, 'login.html', {'msg': 'Invalid password'})
            else:
                return render(request, 'login.html', {'msg': 'Invalid username'})
    return render(request, 'login.html')


def addproduct(request):
    udict=AddCategory.objects.values('cat_name').distinct()
    if request.method == 'POST' and request.FILES['myfile']:
        cat_name = request.POST.get('a1')
        product_name = request.POST.get('a2')
        uom = request.POST.get('a3')
        quantity = request.POST.get('a4')
        price = request.POST.get('a5')
        image = request.POST.get('a6')
        total_stock = request.POST.get('a6')
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        pat = os.path.join(BASE_DIR, '/media/' + filename)

        AddProduct.objects.create(cat_name=cat_name, product_name=product_name, uom=uom, quantity=quantity, price=price,image=myfile, total_stock=total_stock)
        return render(request, 'addproduct.html', {'msg': 'Thank you for adding product','udict':udict})
    return render(request, 'addproduct.html',{'udict':udict})


def addproduct_view(request):
    details = AddProduct.objects.all()
    return render(request, 'addproduct_view.html', {'details': details})


def reg_del(request, pk):
    rdata = UserRegistration.objects.get(id=pk)
    rdata.delete()
    base_url = reverse('reg_view')
    return redirect(base_url)


def product_del(request, pk):
    rdata = AddProduct.objects.get(id=pk)
    rdata.delete()
    base_url = reverse('addproduct_view')
    return redirect(base_url)

def product_edit(request, pk):
    rdata = AddProduct.objects.filter(id=pk).values()
    if request.method == 'POST' and request.FILES['myfile']:
        cat_name = request.POST.get('a1')
        product_name = request.POST.get('a2')
        uom = request.POST.get('a3')
        quantity = request.POST.get('a4')
        price = request.POST.get('a5')
        image = request.POST.get('a6')
        total_stock = request.POST.get('a6')
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        pat = os.path.join(BASE_DIR, '/media/' + filename)

        AddProduct.objects.filter(id=pk).update(cat_name=cat_name, product_name=product_name, uom=uom, quantity=quantity, price=price,image=myfile, total_stock=total_stock)
        base_url=reverse('addproduct_view')
        return redirect(base_url)
    return render(request,'product_edit.html',{'rdata':rdata})



def cat_del(request, pk):
    rdata = AddCategory.objects.get(id=pk)
    rdata.delete()
    base_url = reverse('category_view')
    return redirect(base_url)


def category(request):
    if request.method == 'POST':
        cat_name = request.POST.get('t1')
        AddCategory.objects.create(cat_name=cat_name)
        return render(request, 'category.html', {'msg': 'Thank you for adding product'})
    return render(request, 'category.html')

def category_view(request):
    details = AddCategory.objects.all()
    return render(request,'category_view.html',{'details':details})

def cat_edit(request,pk):
    rdata=AddCategory.objects.filter(id=pk).values()
    if request.method=="POST":
        cat_name = request.POST.get('t1')
        AddCategory.objects.filter(id=pk).update(cat_name=cat_name)
        base_url=reverse('category_view')
        return redirect(base_url)
    return render(request,'cat_edit.html',{'rdata':rdata})


def forgotpass(request):
    if request.method == "POST":
        username = request.POST.get('t1')
        request.session['username']=username
        ucount = UserLogin.objects.filter(username=username).count()
        if ucount >= 1:
            otp = random.randint(1111, 9999)
            OtpCode.objects.create(otp=otp, status='active')
            content = "Your OTP is-" + str(otp)
            smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtp_server.ehlo()
            smtp_server.login('nouman1520@gmail.com', 'wwmuauetiakiqnlf')
            smtp_server.sendmail('nouman1520@gmail.com', username, content)
            smtp_server.close()
            base_url = reverse('otp')
            return redirect(base_url)
        else:
            return render(request, 'forgotpass.html', {'msg': 'Invalid Username'})
    return render(request, 'forgotpass.html')


def otp(request):
    if request.method == "POST":
        otp = request.POST.get('t1')
        count = OtpCode.objects.filter(otp=otp).count()
        if count >= 1:
            base_url = reverse('resetpass')
            return redirect(base_url)
        else:
            return render(request, 'otp.html', {'msg': 'Invalid OTP'})
    return render(request, 'otp.html')


def resetpass(request):
    if request.method == "POST":
        username = request.POST.get('t1')
        username = request.session['username']=username
        newpassword = request.POST.get('t1')
        confirmpassword = request.POST.get('t2')
        if newpassword == confirmpassword:
            UserLogin.objects.filter(username=username).update(password=newpassword)
            base_url = reverse('login')
            return redirect(base_url)
        else:
            return render(request, 'resetpass.html', {'msg': 'newpassword and confirmpassword must be same'})
    return render(request, 'resetpass.html')


def reg_edit(request,pk):
    rdata=UserRegistration.objects.filter(id=pk).values()
    if request.method=="POST":
        name = request.POST.get('t1')
        gender = request.POST.get('r1')
        city = request.POST.get('t2')
        address = request.POST.get('t3')
        pincode = request.POST.get('t4')
        contact = request.POST.get('t5')
        email = request.POST.get('t6')
        UserRegistration.objects.filter(id=pk).update(name=name, gender=gender, city=city, address=address, pincode=pincode,contact=contact, email=email)
        base_url=reverse('reg_view')
        return redirect(base_url)
    return render(request,'reg_edit.html',{'rdata':rdata})


def CustomerOrder(request):
    if request.method == 'POST':
        user_id = request.POST.get('t1')
        product_name = request.POST.get('r1')
        quantity = request.POST.get('t2')
        unit_price = request.POST.get('t3')
        total = request.POST.get('t4')
        order_status = request.POST.get('t5')
        payment_status = request.POST.get('t6')
        MyOrder.objects.create(user_id=user_id,product_name=product_name,quantity=quantity,unit_price=unit_price,total=total,order_status=order_status,payment_status=payment_status)
        return render(request,'CustomerOrder.html',{'msg': 'Thank you for ordering'})
    return render(request,'CustomerOrder.html')


def product_view_user(request):
    pdata=AddProduct.objects.all()
    return render(request,'product_view_user.html',{'pdata':pdata})


def cat_wise_products(request,cat):
    pdata=AddProduct.objects.filter(cat_name=cat).values()
    return render(request,'cat_wise_products.html',{'pdata':pdata})


def add_cart(request,pk):
    user_id=request.session['username']
    pdata=AddProduct.objects.get(id=pk)
    product_name=pdata.product_name
    price=int(pdata.price)
    if request.method=="POST":
        qty=int(request.POST.get('t1'))
        total=qty*price
        MyOrder.objects.create(user_id=user_id,product_name=product_name,quantity=qty,unit_price=price,total=total,order_status='pending',payment_status='pending')
        return render(request,'add_qty.html',{'msg':'Order has been placed successfully'})
    return render(request,'add_qty.html')


def my_cart(request):
    uid=request.session['username']
    udata=MyOrder.objects.filter(order_status='pending').filter(user_id=uid).values()
    return render(request,'my_cart.html',{'udata':udata})

def my_order(request):
    uid=request.session['username']
    udata=MyOrder.objects.filter(order_status='confirmed').filter(user_id=uid).values()
    return render(request,'my_order.html',{'udata':udata})


def remove_cart(request,pk):
    mdata=MyOrder.objects.get(id=pk)
    mdata.delete()
    base_url=reverse('my_cart')
    return redirect(base_url)

def confirm_order(request,pk):
    MyOrder.objects.filter(id=pk).update(order_status='confirmed')
    base_url = reverse('my_cart')
    return redirect(base_url)


def payment(request,pk):
    user_id=request.session['username']
    now=datetime.datetime.now()
    payment_date=now.strftime("%Y-%m-%d")
    udata=MyOrder.objects.get(id=pk)
    total=udata.total
    if request.method=="POST":
        AddPayment.objects.create(order_id=pk,user_id=user_id,payment_date=payment_date,paid_amount=total)
        MyOrder.objects.filter(id=pk).update(payment_status='paid')
        return render(request,'payment.html',{'msg':'Payment has been done successfully'})
    return render(request,'payment.html',{'total':total})
















