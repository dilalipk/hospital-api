from django.urls import path
from . import views

urlpatterns = [
    path("", views.AppointmentView.as_view(), name="appointment"),
    path("doctors/", views.DoctorView.as_view(), name="doctor"),
    path("doctors/<pk>", views.DoctorDetailView.as_view(), name="doctor_detail"),
    path("patients/", views.PatientView.as_view(), name="patient"),
    path("patients/<pk>", views.PatientDetailView.as_view(), name="patient_detail"),
    path("appointments/<pk>", views.AppointmentDetailView.as_view(), name="appointment_detail"),
]
