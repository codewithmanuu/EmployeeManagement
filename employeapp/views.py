from django.shortcuts import render,redirect
from .models import *
from django.shortcuts import get_object_or_404
# Create your views here.
from .forms import *
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from functools import wraps
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
import plotly.graph_objects as go



def custom_login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if 'user_id' not in request.session:
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper
def authenticate(username, password):
    try:
        user = adminmodel.objects.get(username=username)
        if user.password == password:
            return user
    except adminmodel.DoesNotExist:
        return None

def user_login(request):
    if request.method == "POST":
        form = adminform(request.POST)
        if form.is_valid():
            un = form.cleaned_data['username']
            ps = form.cleaned_data['password']
            user = authenticate(un,ps)
            if user is not None:
                request.session['user_id'] = user.id
                return redirect(display_emp)
            else:
                return HttpResponse("failed")

    return render(request, 'log.html')



@custom_login_required
def create_employee(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(display_emp)
        else:
            print(form.errors,'.............>>>>')

    context = {'form': form}
    return render(request, 'employee.html', context)
@custom_login_required
def display_emp(request):
    x=EmployeeModel.objects.all().order_by('id')
    ID=[]
    empid=[]
    fn=[]
    ln=[]
    em=[]
    desi=[]
    tm=[]
    sl=[]
    ph=[]
    for i in x:
        idd=i.id
        ID.append(idd)
        eid=i.EmployeeID
        empid.append(eid)
        f=i.Firstname
        fn.append(f)
        l=i.Lastname
        ln.append(l)
        e=i.email
        em.append(e)
        de=i.designation
        desi.append(de)
        t=i.team
        tm.append(t)
        s=i.salary
        sl.append(s)
        p=i.phonenumber
        ph.append(p)

    mylist=zip(ID,empid,fn,ln,em,desi,tm,sl,ph)
    return render(request,"empdis.html",{'mylist':mylist})
@custom_login_required
def edit_emp(request, id):
    des = Designation.objects.all()
    tem = Team.objects.all()
    prod = EmployeeModel.objects.get(id=id)

    if request.method == "POST":
        prod.EmployeeID = request.POST.get('EmployeeID')
        prod.Firstname = request.POST.get('Firstname')
        prod.Lastname = request.POST.get('Lastname')
        prod.email = request.POST.get('email')
        designation = request.POST.get('AsignDesignation')
        prod.designation=Designation.objects.get(AsignDesignation=designation)
        team = request.POST.get('Createteam')
        prod.team=Team.objects.get(Createteam=team)
        prod.salary = request.POST.get('salary')
        prod.phonenumber = request.POST.get('phonenumber')
        prod.save()
        return redirect(display_emp)

    return render(request, 'editemp.html', {"prod": prod, "des": des, "tem": tem})

@custom_login_required
def create_designation(request):
    desi=desigForm()
    if request.method == 'POST':
        form = desigForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(display_emp)

    context = {'form': desi}
    return render(request,'designation.html',context)
@custom_login_required
def create_team(request):
    desi=teamForm()
    if request.method == 'POST':
        form = teamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(display_emp)

    context = {'form': desi}
    return render(request, 'team.html', context)
@custom_login_required
def Approveleave(request,id):
    emp=EmployeeModel.objects.get(id=id)
    typ=leavetype.objects.all()
    print(typ,"///////")
    if request.method=="POST":
        ty=request.POST.get('type')
        print(request.POST.get('type'),"/////////")
        form=leaveForm(request.POST)
        if form.is_valid():
            fm=form.cleaned_data['fromm']
            t=form.cleaned_data['to']
            lv=leave(user=EmployeeModel.objects.get(id=id),fromm=fm,to=t,type=leavetype.objects.get(ltype=ty))
            lv.save()
            subject = 'leave approved'
            message = f"hii..{lv.user}your leave from{lv.fromm} to {lv.to} is approved"
            recipient = 'ananthup303@gmail.com'
            send_mail(subject,message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            return redirect(leavedis)
    return render(request,'leave.html',{"typ":typ,"emp":emp})
@custom_login_required
def leavedis(request):
    lev=leave.objects.all()
    us=[]
    fr=[]
    to=[]
    ty=[]
    ID=[]
    for i in lev:
        u=i.user
        us.append(u)
        f=i.fromm
        fr.append(f)
        t=i.to
        to.append(t)
        typ=i.type
        ty.append(typ)
        idd=i.id
        ID.append(idd)
    mylist=zip(us,fr,to,ty,ID)
    return render(request,'leavedis.html',{"mylist":mylist})
@custom_login_required
def editleave(request, id):
    user = EmployeeModel.objects.all()
    type = leavetype.objects.all()
    prod = leave.objects.get(id=id)

    if request.method == "POST":

        user = request.POST.get('user')
        prod.user=EmployeeModel.objects.get(Firstname=user)
        prod.fromm = request.POST.get('fromm')
        prod.to = request.POST.get('to')
        type = request.POST.get('type')
        prod.type=leavetype.objects.get(ltype=type)
        prod.save()
        return redirect(leavedis)

    return render(request, 'editleave.html', {"prod": prod, "user": user, "type": type})
@custom_login_required
def deleteleave(request,id):
    lv=leave.objects.get(id=id)
    lv.delete()
    return redirect(leavedis)
@custom_login_required
def empdelete(request,id):
    emp=EmployeeModel.objects.get(id=id)
    emp.delete()
    return redirect(display_emp)
@custom_login_required
def listdesignation(request):
    des=Designation.objects.all()
    return render(request,'listdes.html',{"des":des})
@custom_login_required
def listteam(request):
    tem=Team.objects.all()
    return render(request,'listteam.html',{"tem":tem})

@custom_login_required
def salary_graph(request):
    employees = EmployeeModel.objects.all()
    salaries = [employee.salary for employee in employees]

    fig = go.Figure()
    fig.add_trace(go.Bar(x=[f"Employee {i+1}" for i in range(len(salaries))], y=salaries))
    fig.update_layout(title='Employee Salaries',
                      xaxis_title='Employee',
                      yaxis_title='Salary')

    graph_div = fig.to_html(full_html=False, default_height=500, default_width=700)

    context = {'graph_div': graph_div}
    return render(request, 'graph.html', context)
@custom_login_required
def logout(request):
    del request.session['user_id']
    return redirect('login')

def index(request):
    return render(request,'index.html')