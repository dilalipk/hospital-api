import datetime
from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    )
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    joining_date = models.DateField(default=datetime.date.today)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')
    contact = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " - " + self.contact


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor_appointments')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patient_appointments')
    date = models.DateField(default=datetime.date.today)
    time = models.TimeField(default=datetime.time)
    problem = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.date} - Dr. {self.doctor.name} - {self.patient.name}"
