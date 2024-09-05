from django.urls import path
# from .models import Company
from .import views
from .views import  Experience_certificate
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshSlidingView,TokenVerifyView
from rest_framework.routers import DefaultRouter

rouuter=DefaultRouter()
rouuter.register('dataapi',views.company_data,basename='data')


urlpatterns = [
     
      path('data/',views.company_data,name='data-company'),
      path('update-data/<int:pk>',views.company_data,name='data-company'),

      # path('location-data/',views.location_data,name='data-location'),
      # path('update-location/<int:pk>',views.location_data,name='data-location'),

      path('applicant/', Experience_certificate.as_view(),name='data'),
       path('applicant-data/<int:pk>', Experience_certificate.as_view(),name='data'),
      #  path('applicant-data/<int:pk>', Experience_certificate.as_view(),name='data'),
       
       path('gettoken/',TokenObtainPairView.as_view(),name='token_obtain'),     # access or refresh token generate kar ke dega
      path('refreshtoken/',TokenRefreshSlidingView.as_view(),name='token_refresh'), # refresh 
      path('verifytoken/',TokenVerifyView.as_view(),name='token_verify'), # token valid he ya nahi ye chek karega
  
]