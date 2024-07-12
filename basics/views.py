from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, redirect
from .models import EmployeeDetails


def registration(request):
    if request.method == 'POST':
        username = request.POST['textusername']
        firstname = request.POST['textfirstname']
        lastname = request.POST['textlastname']
        email = request.POST['textemail']
        password = make_password(request.POST['textpassword'])  

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already exists')
            return render(request, 'registration.html')
        else:
            user = User(username=username, first_name=firstname, last_name=lastname, email=email, password=password)
            user.save()
            messages.success(request, 'Registration successful')
            return render(request, 'registration.html')
    else:
        return render(request, 'registration.html')


def userlogin(request):
  if request.method=="POST":
    data=request.POST
    username=data.get('textusername')
    password=data.get('textpassword')
    user= User.objects.filter(username=username)
    if not user.exists():
       result="Invalid username"
       return render(request,'login.html',context={'result':result})
    user= authenticate(username=username,password=password)
    if(user is None):
       result="Invalid Password"
       return render(request,'login.html',context={'result':result})
    else:
       login(request,user)
       return redirect('/dashboard/')
    
  return render(request,'login.html')

def userlogout(request):
   logout(request)
   return redirect('/userlogin')


def index(request):
    return render(request, 'index.html')


def menu(request):
    return render(request, 'menu.html')


def NavBar(request):
    return render(request, 'NavBar.html')



from django.shortcuts import render, redirect, get_object_or_404
from .models import EmployeeDetails
from django.http import Http404

def employeedetailsview(request, employee_id=None):
    result_message = None

    # Fetch all employees
    result = EmployeeDetails.objects.all()

    if request.method == "POST":
        if 'add_employee' in request.POST:
            # Add employee
            data = request.POST
            empid = data.get('textempid')
            empname = data.get('textempname')
            empcompid = data.get('textempcompid')
            empmailid = data.get('textempmailid')
            empphoneno = data.get('textempphoneno')
            empdoj = data.get('textempdoj')
            emprolename = data.get('textemprolename')

            EmployeeDetails.objects.create(
                EMP_ID=empid,
                EMP_NAME=empname,
                EMP_COMP_ID=empcompid,
                EMP_MAILID=empmailid,
                EMP_PHONENO=empphoneno,
                EMP_DOJ=empdoj,
                EMP_ROLE_NAME=emprolename
            )
            result_message = "Employee details saved successfully"

        elif 'update_employee' in request.POST:
            # Update employee
            update_data = request.POST
            update_id = update_data.get('employee_id')
            try:
                emp = EmployeeDetails.objects.get(id=update_id)
                emp.EMP_ID = update_data.get('textempid')
                emp.EMP_NAME = update_data.get('textempname')
                emp.EMP_COMP_ID = update_data.get('textempcompid')
                emp.EMP_MAILID = update_data.get('textempmailid')
                emp.EMP_PHONENO = update_data.get('textempphoneno')
                emp.EMP_DOJ = update_data.get('textempdoj')
                emp.EMP_ROLE_NAME = update_data.get('textemprolename')
                emp.save()
                result_message = "Employee details updated successfully"
            except EmployeeDetails.DoesNotExist:
                raise Http404("Employee does not exist")

    return render(request, 'employeedetailsview.html', context={'result': result, 'result_message': result_message})


def employeedetailsdelete(request,id):
    result= EmployeeDetails.objects.get(id=id)
    result.delete()
    return redirect('/employeedetailsview/')


from django.shortcuts import render
from .models import VisitorDetails, EmployeeDetails
from django.db.models import Count
import datetime

def dashboard(request):
    # Fetching the required statistics from the database
    total_visitors = VisitorDetails.objects.count()
    total_employees = EmployeeDetails.objects.count()

    today_str = datetime.date.today().strftime('%Y-%m-%d')
    checkins_today = VisitorDetails.objects.filter(VS_DATE=today_str).count()
    pending_approvals = VisitorDetails.objects.filter(status='Pending').count()
    visitors_inside = VisitorDetails.objects.filter(status='Inside').count()

    # Fetching additional data related to employees
    employees_name = EmployeeDetails.objects.values('EMP_NAME').annotate()
    
    # Fetching visitor names
    visitor_names = VisitorDetails.objects.values('VS_NAME').distinct()

    # Creating the context to pass to the template
    context = {
        'total_visitors': total_visitors,
        'total_employees': total_employees,
        'checkins_today': checkins_today,
        'pending_approvals': pending_approvals,
        'visitors_inside': visitors_inside,
        'employees_name': employees_name,
        'visitor_names': visitor_names,  # corrected variable name
    }

    # Rendering the dashboard template with the context
    return render(request, 'dashboard.html', context)

from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import VisitorDetails, VisitorRequest

def visitordetailsview(request):
    result_message = None
    result = VisitorDetails.objects.all()

    if request.method == "POST":
        if 'add_visitor' in request.POST:
            # Handle adding a new visitor directly
            data = request.POST
            VisitorDetails.objects.create(
                VS_ID=data.get('textvsid'),
                VS_NAME=data.get('textvsname'),
                VS_DATE=data.get('textvsdate'),
                VS_PHONENO=data.get('textvsphoneno'),
                VS_MAILID=data.get('textvsmailid'),
                VS_PURPOSE=data.get('textvspurpose'),
                VS_REMARKS=data.get('textvsremarks'),
                status='Approved'
            )
            result_message = "Visitor added successfully"

        elif 'update_visitor' in request.POST:
            # Handle updating an existing visitor
            update_data = request.POST
            update_id = update_data.get('visitor_id')
            try:
                vs = VisitorDetails.objects.get(id=update_id)
                vs.VS_ID = update_data.get('textvsid')
                vs.VS_NAME = update_data.get('textvsname')
                vs.VS_DATE = update_data.get('textvsdate')
                vs.VS_PHONENO = update_data.get('textvsphoneno')
                vs.VS_MAILID = update_data.get('textvsmailid')
                vs.VS_PURPOSE = update_data.get('textvspurpose')
                vs.VS_REMARKS = update_data.get('textvsremarks')
                vs.save()
                result_message = "Visitor details updated successfully"
            except VisitorDetails.DoesNotExist:
                raise Http404("Visitor does not exist")

    return render(request, 'visitordetailsview.html', context={'result': result, 'result_message': result_message})

def visitordetailsdelete(request, id):
    result = get_object_or_404(VisitorDetails, id=id)
    result.delete()
    return redirect('/visitordetailsview/')

def admin_approval(request):
    pending_visitors = VisitorRequest.objects.filter(is_approved=False)
    return render(request, 'admin_approval.html', {'pending_visitors': pending_visitors})

def admin_approve(request, id):
    visitor_request = get_object_or_404(VisitorRequest, id=id)
    VisitorDetails.objects.create(
        VS_ID=visitor_request.VS_ID,
        VS_NAME=visitor_request.VS_NAME,
        VS_DATE=visitor_request.VS_DATE,
        VS_PHONENO=visitor_request.VS_PHONENO,
        VS_MAILID=visitor_request.VS_MAILID,
        VS_PURPOSE=visitor_request.VS_PURPOSE,
        VS_REMARKS=visitor_request.VS_REMARKS,
        status='Approved'
    )
    visitor_request.is_approved = True
    visitor_request.save()
    return redirect('admin_approval')

def admin_reject(request, id):
    visitor_request = get_object_or_404(VisitorRequest, id=id)
    visitor_request.delete()
    return redirect('admin_approval')

    

from django.shortcuts import render, redirect
from django.http import Http404
from .models import VisitorDetails, VisitorRequest

def home(request):
    result_message = None

    if request.method == "POST":
        if 'request_visit' in request.POST:
            # Handle visitor request submission
            data = request.POST
            VisitorRequest.objects.create(
                VS_ID=data.get('textvsid'),
                VS_NAME=data.get('textvsname'),
                VS_DATE=data.get('textvsdate'),
                VS_PHONENO=data.get('textvsphoneno'),
                VS_MAILID=data.get('textvsmailid'),
                VS_PURPOSE=data.get('textvspurpose'),
                VS_REMARKS=data.get('textvsremarks')
            )
            result_message = "Visitor request submitted successfully and awaiting approval"

    # Include 'result_message' in the context when rendering 'home.html'
    return render(request, 'home.html', context={'result_message': result_message})




