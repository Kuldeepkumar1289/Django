from django.urls import path
from .import views

urlpatterns=[
    path('sign_in_admin',views.sign_in_admin,name='sign_in_admin'),
    path('signup+patient',views.sign_in_patient,name="sign_in_patient"),
    path('signup+patient',views.signup_patient,name='sign_in_patient'),
    path('savepdata/<str:patientusername>',views.savepdata,name='savepdata'),



    path('signup_doctor',views.signup_doctor,name='signup_doctor'),
    path('sign_in_doctor',views.sign_in_doctor,name="sign_in_doctor"),
    path('savepdata/<str:doctorusername>',views.savepdata,name='savedata'),

    path('logout',views.logout,name='logout'),

]