#it is where you can define the logic that handles user requests and return responses
#views are responsible for processing the input(request), interacting with model to retrieve or manipulate data, and then render the template to produce the output
#handle request- views receive the HTTP requests from the user, these requests can be of different types of operations such as displaying a webpage,
#submitting a form, or interacting with an API
# process data - Views interact with the models to perform data-related operations. This can include querying the database, saving new data, updating existing data, or deleting data.
# render template - Views interact with the models to perform data-related operations. This can include querying the database, saving new data, updating existing data, or deleting data.
#return responses - Finally, views return an HTTP response to the user. This response could be an HTML page, a redirect, a JSON response (in the case of APIs), or other types of responses.
#Types of Views - Types of Views1. *Function-Based Views (FBVs)*: These are defined as simple Python functions. The above example uses function-based views.
#2. *Class-Based Views (CBVs)*: These are defined using Python classes, which can provide more structure and reusable code. 



from django.shortcuts import render , HttpResponse
from .models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request,'index.html')


def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request,'all_emp.html', context)


def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        new_emp= Employee(first_name= first_name, last_name= last_name, salary= salary, bonus = bonus, phone = phone, dept_id = dept, role_id = role, hire_date = datetime.now()  )
        new_emp.save()
        return HttpResponse('Employee added successfully')
    
    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("An Error has Occured!")


def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully!")
        except:
            return HttpResponse("Please Enter A Valid EMP ID")
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request,'remove_emp.html', context)


def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name)) # agar kisi ka name harsh hai or apan ne hrsh type kara to iss methord se vo apan ko real name sujjest karta hai.
        if dept:
            emps = emps.filter(emps__name__icontains = dept) # yahi likhne ka tarika hota hai model__field 
        if role:
            emps = emps.filter(emps__name__icontains = role) 

        context = {
            'emps' : emps
        }       
        return render(request, 'all_emp.html', context)
    
    elif request.method == 'GET':
        return render(request,'filter_emp.html')
    else:
        return HttpResponse('An exception occured!')
    
