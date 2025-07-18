from django.db import models

# Create your models here.
class employee_detail(models.Model):
    name = models.CharField(max_length=30)
    date_of_birth =models.DateField()
    mobile_number=models.CharField(max_length=30)
    email_id=models.EmailField(max_length=254)
    gender=models.CharField(max_length=30)
    
    # address=models.CharField(max_length=255)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    
    department=models.CharField(max_length=30)
    designation=models.CharField(max_length=30)
    salary=models.IntegerField()
    year_of_exp=models.IntegerField()
    join_date=models.DateField()
    
class employee_details(models.Model):
    name = models.CharField(max_length=30)
    date_of_birth =models.DateField()
    mobile_number=models.CharField(max_length=30)
    email_id=models.EmailField(max_length=254)
    gender=models.CharField(max_length=30)
    
    # address=models.CharField(max_length=255)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    
    department=models.CharField(max_length=30)
    designation=models.CharField(max_length=30)
    salary=models.IntegerField()
    year_of_exp=models.IntegerField()
    join_date=models.DateField()
