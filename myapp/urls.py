from django.urls import path
# from .models import Company
from .import views
from .views import  Experience_certificate


urlpatterns = [
     
      path('data/',views.company_data,name='data-company'),
      path('update-data/<int:pk>',views.company_data,name='data-company'),

      # path('location-data/',views.location_data,name='data-location'),
      # path('update-location/<int:pk>',views.location_data,name='data-location'),

      path('applicant/', Experience_certificate.as_view(),name='data'),
       path('applicant-data/<int:pk>', Experience_certificate.as_view(),name='data'),
       path('applicant-data/<int:pk>', Experience_certificate.as_view(),name='data'),
      
  
]