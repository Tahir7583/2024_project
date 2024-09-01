from django.db import models

# Create your models here.

class Company (models.Model):
    company_name=models.CharField(max_length=500)
    phone=models.IntegerField() 
    email=models.EmailField()
    website=models.CharField(max_length=500)
    founded_data=models.DateField(default=True)
    company_size=models.IntegerField()
    logo=models.ImageField(null=True)
    description=models.TextField()


class Location(models.Model):
    company_id=models.ForeignKey(Company,related_name="company_id",on_delete=models.CASCADE)
    address=models.CharField(max_length=500)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    postal_code=models.IntegerField()
    country=models.CharField(max_length=100)



  
class ApplicantExperince(models.Model): 
    company_name=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    description=models.TextField()
    department=models.CharField(max_length=100)
    salary=models.IntegerField()
    start_date=models.DateField()
    end_date=models.DateField(null=True)

class Applicant_certificate(models.Model):
    applicant_id=models.ForeignKey(ApplicantExperince,on_delete=models.CASCADE,related_name='applicant_id')
    certificate_name=models.CharField(max_length=100)
    issuing_orgnization=models.CharField(max_length=100)
    issue_date=models.DateField()
    certificate=models.ImageField(null=True)


    


