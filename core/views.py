from django.shortcuts import render


def landing(request):
    return render(request, "landing.html")


def login(request):
    return render(request, "login.html")

def patient_dashboard(request):
    #patient = request.user.patient_profile
    patient = {
        "name": "Daniel Wong",
        "patient_id": "PT-10528",
        "phone": "+62 812-9012-4477",
        "email": "daniel.wong@example.com",
        "address": "31, Kaliurang Rd, Yogyakarta",
        "age": 42,
        "gender": "Male",
        "date_of_birth": "23 July 1983",
        "blood_type": "O+",
        "occupation": "Project Manager",
        "status": "Post-Op Inpatient",
        "insurance": "BPJS – Class 1",
    }

    return render(
        request,
        "patient/dashboard.html",
        {
            "page_title": "Patient Dashboard",
            "breadcrumb": "Patient / Dashboard",
            "patient": patient,
        },
    )


def patient_details(request):
    return render(
        request,
        "patient/patient_details.html",
        {
            "page_title": "Patient Details",
            "breadcrumb": "Patient / Details",
        },
    )


def patient_appointments(request):
    return render(
        request,
        "patient/appointments.html",
        {
            "page_title": "Appointments",
            "breadcrumb": "Patient / Appointments",
        },
    )


def patient_medical_records(request):
    return render(
        request,
        "patient/medical_records.html",
        {
            "page_title": "Medical Records",
            "breadcrumb": "Patient / Medical Records",
        },
    )


def patient_profile(request):
    return render(
        request,
        "patient/profile.html",
        {
            "page_title": "My Profile",
            "breadcrumb": "Patient / Profile",
        },
    )