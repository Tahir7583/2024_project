from rest_framework import serializers
from .models import Company,Location,ApplicantExperince,Applicant_certificate


class Companyserializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields="__all__"
        depth=1
      


class Locationserializer(serializers.ModelSerializer):
 
  class Meta:
        model=Location
        fields="__all__"
        depth=1
   


class applicant_Ex_serializer(serializers.ModelSerializer):
    class Meta :
        model=ApplicantExperince
        fields="__all__"
        
    
      

class applicant_cert_serializer(serializers.ModelSerializer): 
    # data = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta :
        model=Applicant_certificate
        # fields=['id','certificate_name','issuing_orgnization','issue_date','certificate','data']
        fields='__all__'
        depth=1
      
    
   
      

 




