from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing, name="landing"),
    path("login/", views.login, name="login"),
    path("patient/", views.patient_dashboard, name="patient_dashboard"), path("patient/details/", views.patient_details, name="patient_details"), path("patient/appointments/", views.patient_appointments, name="patient_appointments"), path("patient/medical-records/", views.patient_medical_records, name="patient_medical_records"), path("patient/profile/", views.patient_profile, name="patient_profile"),
]