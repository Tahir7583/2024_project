from rest_framework import serializers
from .models import Company,Location,ApplicantExperince,Applicant_certificate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



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


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
        # Pehle default validation call karte hain
    def validate (self,attrs):  # self hamare object ko point karta he attrs atribute they are accept data comeing from login
        data = super().validate(attrs)  #  token generate kar ke data object me save hoga
        
       #custom data
        if self.user.is_superuser:    #yaha  superuser agr exist karta he to admin verify hoga or token me save ho jayga
            data['admin'] = self.user.is_superuser      # jis ko data edit karne ki access hogi
            data['email']=self.user.email
        else:
            data['role'] = 'user'    #agr if conditon me superuser true nahi he to else me chek hoga normal 
                                        #user jis ke pas sirf data dekhne ki access rahegi 
    
            data['email']='email'
                                            
        return data
      
    
   
      

 




