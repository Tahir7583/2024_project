from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from . models import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated



# Create your views here.

@api_view(['GET','POST','PUT','DELETE'])
@permission_classes([IsAuthenticated])   # decorator se permission class ka use kar ke authantication implement
@authentication_classes([JWTAuthentication]) 
def company_data(request,pk=None):
   if request.method=='GET':
        obj=Location.objects.all()
        serializer=Locationserializer(obj,many=True)
        return Response (serializer.data)
    
    

   elif request.method=='POST': 
        jsondata=request.data 
        company_Data={
            'company_name':jsondata["company_name"],
            'phone':jsondata['phone'],
            'email':jsondata['email'],
            'website':jsondata['website'],
            'founded_data':jsondata['founded_data'],
            'company_size':jsondata['company_size'],
            'logo':jsondata['logo'],
            'description':jsondata['description']

        }
        location_Data={
           # 'company_id':jsondata['company_id'],
            'address':jsondata['address'],
            'city': jsondata['city'],
            'state':jsondata['state'],
            'postal_code':jsondata['postal_code'],
            'country':jsondata['country']

        }
        company_obj=Company.objects.create(**company_Data)
        company_obj.save()
        location_obj=Location.objects.create(company_id=company_obj, **location_Data)

        serializer=Locationserializer(location_obj,data=jsondata)
        if serializer.is_valid():
            serializer.save()
            return Response ('new location and  company add  successfully')
        return Response ('enter valid data ')
   
   
   
   
   elif request.method=='PUT': 
        jsondata=request.data 
        company_Data={
            'company_name':jsondata["company_name"],
            'phone':jsondata['phone'],
            'email':jsondata['email'],
            'website':jsondata['website'],
            'founded_data':jsondata['founded_data'],
            'company_size':jsondata['company_size'],
            'logo':jsondata['logo'],
            'description':jsondata['description']

        }
        location_Data={
           # 'company_id':jsondata['company_id'],
            'address':jsondata['address'],
            'city': jsondata['city'],
            'state':jsondata['state'],
            'postal_code':jsondata['postal_code'],
            'country':jsondata['country']
        }

        location_obj=Location.objects.get(id=pk)
        company_id=location_obj.company_id.id
        company_obj=Company.objects.get(id=company_id)

        L_serializer=Locationserializer(location_obj,data=location_Data)
        C_serializer=Companyserializer(company_obj,data=company_Data)

        if  L_serializer.is_valid():
            L_serializer.save()

        if  C_serializer.is_valid():
            C_serializer.save()
            return Response ('update successfully')
        return Response ('valid data please')
   
   
   
   elif request.method=='DELETE':
        Data=request.data
        obj=Company.objects.get(id=pk)
        obj.delete()
        return Response ('delete successfully') 
    



    



    

                    #class based views
    



class Experience_certificate (APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]


    def get(self,request,pk=None):
        Data=Applicant_certificate.objects.all()
        serializer=applicant_cert_serializer(Data,many=True)
        return Response (serializer.data)
    



    

    def post(self,request,pk=None):
        jsondata=request.data 
        ApplicantExperince_Data={
            'company_name':jsondata["company_name"],
            'designation':jsondata['designation'],
            'department':jsondata['department'],
            'salary':jsondata['salary'],
            'start_date':jsondata['start_date'],
            'end_date':jsondata['end_date']

        }
        Applicant_certificate_Data={
            #'applicant_id': jsondata.get['applicant_id'],
            #'company_id':jsondata.get['company_id'],
            'certificate_name': jsondata['certificate_name'],
            'issuing_orgnization':jsondata['issuing_orgnization'],
            'issue_date':jsondata['issue_date'],
            'certificate':jsondata['certificate']

        }
     
        applicant_ex_data=ApplicantExperince.objects.create(**ApplicantExperince_Data)
        
        applicant_ex_data.save()
       

        applicant_cer_data=Applicant_certificate.objects.create(applicant_id=applicant_ex_data, **Applicant_certificate_Data)
        applicant_cer_data.save()

        serializer=applicant_Ex_serializer(applicant_cer_data,data=jsondata)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response (' add  successfully')
        return Response ('enter valid data')
    



    


    def put(self ,request,pk=None):
    
        jsondata=request.data
        ApplicantExperince_Data={
            'company_name':jsondata["company_name"],
            'designation':jsondata['designation'],
            'department':jsondata['department'],
            'salary':jsondata['salary'],
            'start_date':jsondata['start_date'],
            'end_date':jsondata['end_date']

        }
        Applicant_certificate_Data={
         
            'certificate_name': jsondata['certificate_name'],
            'issuing_orgnization':jsondata['issuing_orgnization'],
            'issue_date':jsondata['issue_date'],
            'certificate':jsondata['certificate']

        }

        experince_obj=Applicant_certificate.objects.get(id=pk) 
        print(experince_obj) 
     
        applicant_id=experince_obj.applicant_id.id
        applicantEX_obj=ApplicantExperince.objects.get(id=applicant_id)

        serializer1=applicant_Ex_serializer(applicantEX_obj,data=ApplicantExperince_Data)
        print(serializer1)
        serializer2=applicant_cert_serializer(experince_obj,data=Applicant_certificate_Data)

        if serializer1.is_valid():
            serializer1.save()

        if serializer2.is_valid():
            serializer2.save()

            return Response ('update data successfully')
        return Response ('not a valid data')
    


    def delete(self,request,pk=None):
        jsondata=request.data 
        obj=ApplicantExperince.objects.get(id=pk)
        if obj:
            obj.delete()
            return Response ('delete sucessfully')
    



    