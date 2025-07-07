from django.shortcuts import render,redirect
from .models import  employee_detail, employee_details

# Create your views here.
def form(request):
    return render(request, 'form.html')

def table_data(request):
    return render(request,'table_data.html')

def show_data(request):
    return render(request,'show_data.html')

def add_details(request):
     if request.method == "POST":
        n = request.POST["name"]
        dob = request.POST["dob"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        gender = request.POST["gender"]

        street = request.POST["street"]
        city = request.POST["city"]
        state = request.POST["state"]
        zip_code = request.POST["zip"]
        
        department = request.POST["department"]
        designation = request.POST["designation"]
        salary = request.POST["salary"]
        experience = request.POST["experience"]
        join_date = request.POST["join"]

        employee_details.objects.create(
            name=n,date_of_birth=dob,mobile_number=phone,email_id=email,gender=gender,
            street=street,city=city,
            state=state,zip_code=zip_code,department=department,designation=designation,
            salary=salary,year_of_exp=experience,join_date=join_date
        )

        print("Employee added")
        all_employees = employee_details.objects.all()
        return render(request,'table_data.html',{'users': all_employees})
    
def show_details(request):
     all_employees = employee_details.objects.all()
     return render(request,'show_data.html',{'users': all_employees})
 
def find_person(request):
     n = request.GET.get("N")
     person=employee_details.objects.filter(name__icontains=n).values()
     return render(request, 'table_data.html', {'users': person})
 
def update_all(request,id):
    print(id)
    u=employee_details.objects.get(id=id)
    d={"u":u}
    return render(request,'updateform.html',d)

def update_employee(request):
    if request.method=="POST":
        id = request.POST["id"] 
        n = request.POST["name"]
        dob = request.POST["dob"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        gender = request.POST["gender"]

        street = request.POST["street"]
        city = request.POST["city"]
        state = request.POST["state"]
        zip_code = request.POST["zip"]
        
        department = request.POST["department"]
        designation = request.POST["designation"]
        salary = request.POST["salary"]
        experience = request.POST["experience"]
        join_date = request.POST["join"]
        employee_details.objects.filter(id=id).update( name=n,date_of_birth=dob,mobile_number=phone,email_id=email,gender=gender,
            street=street,city=city,
            state=state,zip_code=zip_code,department=department,designation=designation,
            salary=salary,year_of_exp=experience,join_date=join_date)
        return redirect(show_details)
    
def confirm_delete(request, id):
    u = employee_details.objects.get(id=id)
    return render(request, 'delete_data.html', {'u': u})


def delete_data(request, id):
    employee = employee_details.objects.get(id=id)
    employee.delete()
    return redirect(show_details)

    
    