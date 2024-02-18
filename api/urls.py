from django.urls import path
from . import views

urlpatterns = [
    path("", views.AppointmentView.as_view(), name="appointment"),
    path("doctor/", views.DoctorView.as_view(), name="doctor"),
    path("doctor/<pk>", views.DoctorDetailView.as_view(), name="doctor_detail"),
    path("patient", views.PatientView.as_view(), name="patient"),
    path("patient/<pk>", views.PatientDetailView.as_view(), name="patient_detail"),
    path("app/<pk>", views.AppointmentDetailView.as_view(), name="appointment_detail"),
]
