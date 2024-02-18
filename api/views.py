from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Appointment, Patient, Doctor
from .serializer import AppointmentSerializer, PatientSerializer, DoctorSerializer


# Create your views here.


class AppointmentView(APIView):

    def get(self, request):
        appointment = Appointment.objects.all()
        serializer = AppointmentSerializer(appointment, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientView(APIView):

    def get(self, request):
        patient = Patient.objects.all()
        serializer = PatientSerializer(patient, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DoctorView(APIView):

    def get(self, request):
        doctor = Doctor.objects.all()
        serializer = DoctorSerializer(doctor, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AppointmentDetailView(APIView):

    def get(self, request, pk):
        try:
            appointment = Appointment.objects.get(pk=pk)
            serializer = AppointmentSerializer(appointment, many=False)
            return Response(serializer.data)
        except Appointment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            appointment = Appointment.objects.get(pk=pk)
            serializer = AppointmentSerializer(appointment, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Appointment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            appointment = Appointment.objects.get(pk=pk)
            appointment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Appointment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class PatientDetailView(APIView):
    def get(self, request, pk):
        try:
            patient = Patient.objects.get(pk=pk)
            serializer = PatientSerializer(patient, many=False)
            return Response(serializer.data)
        except Patient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk):
        try:
            patient = Patient.objects.get(pk=pk)
            serializer = PatientSerializer(patient, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Patient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk):
        try:
            patient = Patient.objects.get(pk=pk)
            patient.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Patient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        


class DoctorDetailView(APIView):
    def get(self, request, pk):
        try:
            doctor = Doctor.objects.get(pk=pk)
            serializer = DoctorSerializer(doctor, many=False)
            return Response(serializer.data)
        except Doctor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk):
        try:
            doctor = Doctor.objects.get(pk=pk)
            serializer = DoctorSerializer(doctor, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Doctor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk):
        try:
            doctor = Doctor.objects.get(pk=pk)
            doctor.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Doctor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

    