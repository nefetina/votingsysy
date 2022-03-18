from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import newreg
from .models import candidates
from .models import comelecreg
import mysql.connector as sql

installed_apps = ['votingsysApp']

# Create your views here.
def index(request):#login student
    return render(request, 'votingsysApp/index.html')

def newreg1(request):# signup student
    return render(request, 'votingsysApp/newreg.html')

# student registration
def new(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        idno = request.POST.get('idno')
        password = request.POST.get('password')
        # confirm_password = request.POST.get('confirm_password'),
        data = newreg.objects.create(name=name, email=email, idno=idno, password=password)
        data.save()
        return render(request, 'votingsysApp/index.html')



def comeleclog(request):# comelec login
    return render(request, 'votingsysApp/comelec_login.html')

def regcomelec(request):# comelec signup
    return render(request, 'votingsysApp/comelec_reg.html')


# -------comelec registration
def regcom(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        idno = request.POST.get('idno')
        pas = request.POST.get('pas')
        # cpassword = request.POST.get('cpassword'),
        data = comelecreg.objects.create(name=name, email=email, idno=idno, password=pas)
        data.save()
        return render(request, 'votingsysApp/comelec_login.html')


# ------comelec log in
def comlog(request):
    if request.method=="POST":
        n=sql.connect(host="localhost",user="root",password="",database='vsdb')
        cursor=n.cursor()
        e=request.POST
        for key,value in e.items():
            if key=="email":
                email=value
            if key=="pass":
                password=value
        
        l="select * from votingsysapp_comelecreg where email='{}' and password='{}'".format(email,password)
        
        cursor.execute(l)
        h=tuple(cursor.fetchall())
        if h==():
            return render(request, 'votingsysApp/comelec_login.html')
            
        else:
            data = comelecreg.objects.filter(email=email)
          
            return redirect('/comelec', {'data':data})

    return render(request, 'votingsysApp/comeleclog.html')


#     user login


# def login(request):
#     if request.method=='POST':
#         username = request.POST.get('email')
#         password = request.POST.get('pass')
#         user = authenticate(username=username, password=password)
    


def userlogin(request):
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password="",database='vsdb')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                email=value
            if key=="pass":
                password=value
        
        c="select * from votingsysapp_newreg where email='{}' and password='{}'".format(email,password)
        
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request, 'votingsysApp/index.html')
            
        else:
            data = newreg.objects.filter(email=email)
          
            return render(request, 'votingsysApp/homepage.html', {'data':data})

    return render(request, 'votingsysApp/index.html')
         

#                  candidates


def peoples(request):
    if request.method=='POST':
        firstname = request.POST.get('firstname')
        surname = request.POST.get('surname')
        course = request.POST.get('course')
        age = request.POST.get('age')
        gender=request.POST.get('gender')
        position=request.POST.get('position')
        partylist=request.POST.get('partylist')
        image=request.POST.get('image')
        lala=request.POST.get('lala')
        
        datas = candidates.objects.create(firstname=firstname, surname=surname, course=course, age=age, gender=gender, position=position, partylist=partylist, image=image, description=lala)
        datas.save()
    
        return redirect('/homepage')
    
    
def delete(request, id):
    data = candidates.objects.get(id=id)
    data.delete()
    return redirect('/comelec')

def homepage(request):
    data = newreg.objects.all()
    return render(request, 'votingsysApp/homepage.html', {'data':data})

def result(request):
    return render(request, 'votingsysApp/result.html')

def comelec(request):
    nef1 = candidates.objects.all()
    return render(request, 'votingsysApp/comelec.html', {'nef1':nef1})

def application(request):
    return render(request, 'votingsysApp/application.html')




