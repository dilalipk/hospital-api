# Doctor-Patient Appointment API

Welcome to the Doctor-Patient Appointment API documentation. This API, built using Django REST Framework, facilitates the management of doctor-patient appointments.

## Overview

The Doctor-Patient Appointment API allows for the creation, retrieval, updating, and deletion of appointments between doctors and patients.

## Features

- Create, retrieve, update, and delete appointments
- Retrieve lists of doctors, patients, and appointments
- Error handling


## Endpoints

### Doctors

- `GET /api/doctors/`: Retrieve a list of all doctors
- `POST /api/doctors/`: Create a new doctor profile
- `GET /api/doctors/<pk>/`: Retrieve details of a specific doctor
- `PUT /api/doctors/<pk>/`: Update details of a specific doctor
- `DELETE /api/doctors/<pk>/`: Delete a doctor profile

### Patients

- `GET /api/patients/`: Retrieve a list of all patients
- `POST /api/patients/`: Create a new patient profile
- `GET /api/patients/<pk>/`: Retrieve details of a specific patient
- `PUT /api/patients/<pk>/`: Update details of a specific patient
- `DELETE /api/patients/<pk>/`: Delete a patient profile

### Appointments

- `GET /appointments/`: Retrieve a list of all appointments
- `POST /api/appointments/`: Create a new appointment
- `GET /api/appointments/<pk>/`: Retrieve details of a specific appointment
- `PUT /api/appointments/<pk>/`: Update details of a specific appointment
- `DELETE /api/appointments/<pk>/`: Cancel a specific appointment

## Error Handling

The API provides error handling, returning appropriate HTTP status codes and error messages to aid in debugging and troubleshooting.
