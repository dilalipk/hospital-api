from rest_framework import serializers
from .models import Appointment, Patient, Doctor
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "name",
        ]

    def get_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ["name", "contact"]


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ["name", "specialization"]


class AppointmentSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer()
    patient = PatientSerializer()
    created_by = UserSerializer()

    class Meta:
        model = Appointment
        exclude = ["created_at", "updated_at"]
