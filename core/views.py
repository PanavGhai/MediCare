from django.shortcuts import render


def landing(request):
    return render(request, "landing.html")


def login(request):
    return render(request, "login.html")

def patient_dashboard(request):
    # TODO: Replace all sample data below with injectable/database-backed patient data later.
    # patient = request.user.patient_profile

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
        "status": "Active",
        "insurance": "BPJS – Class 1",
    }

    # TODO: Replace with patient health metrics from the database/service layer.
    health_metrics = {
        "blood_sugar": {
            "value": 171,
            "unit": "mg/dL",
        },
        "body_weight": {
            "value": 62,
            "unit": "kg",
        },
        "temperature": {
            "value": 37,
            "unit": "°C",
        },
    }

    # TODO: Replace with patient blood pressure readings from the database/service layer.
    blood_pressure = {
        "last_checkup": "Dec, 2026",
        "monthly_readings": [
            {
                "month": "Jan",
                "systolic": 128,
                "diastolic": 82,
                "heart_rate": 72,
            },
            {
                "month": "Feb",
                "systolic": 124,
                "diastolic": 80,
                "heart_rate": 76,
            },
            {
                "month": "Mar",
                "systolic": 121,
                "diastolic": 79,
                "heart_rate": 74,
            },
            {
                "month": "Apr",
                "systolic": 126,
                "diastolic": 81,
                "heart_rate": 78,
            },
            {
                "month": "May",
                "systolic": 130,
                "diastolic": 84,
                "heart_rate": 80,
            },
            {
                "month": "Jun",
                "systolic": 127,
                "diastolic": 82,
                "heart_rate": 77,
            },
            {
                "month": "Jul",
                "systolic": 123,
                "diastolic": 78,
                "heart_rate": 73,
            },
            {
                "month": "Aug",
                "systolic": 119,
                "diastolic": 76,
                "heart_rate": 71,
            },
            {
                "month": "Sep",
                "systolic": 122,
                "diastolic": 78,
                "heart_rate": 74,
            },
            {
                "month": "Oct",
                "systolic": 125,
                "diastolic": 80,
                "heart_rate": 76,
            },
            {
                "month": "Nov",
                "systolic": 129,
                "diastolic": 83,
                "heart_rate": 79,
            },
            {
                "month": "Dec",
                "systolic": 126,
                "diastolic": 81,
                "heart_rate": 75,
            },
        ],
    }

    # TODO: Replace with prescription records from the database/service layer.
    prescriptions = [
        {
            "name": "Paracetamol Tablet",
            "dosage": "500 mg",
            "frequency": "Every 8 hours as needed",
            "start_date": "11 Mar 2026",
            "end_date": None,
            "status": "Active",
            "category": "active",
        },
        {
            "name": "Etocoxib Injection",
            "dosage": "40 mg",
            "frequency": "Once daily",
            "start_date": "11 Mar 2026",
            "end_date": None,
            "status": "Active",
            "category": "active",
        },
        {
            "name": "Amlodipine Tablet",
            "dosage": "5 mg",
            "frequency": "Once daily (morning)",
            "start_date": "03 Jan 2026",
            "end_date": "08 Mar 2026",
            "status": "Discontinued",
            "category": "discontinued",
        },
        {
            "name": "Ibuprofen Tablet",
            "dosage": "400 mg",
            "frequency": "Twice daily",
            "start_date": "15 Jan 2026",
            "end_date": "29 Jan 2026",
            "status": "Completed",
            "category": "history",
        },
    ]

    # TODO: Replace with appointment records from the database/service layer.
    appointments = [
        {
            "date": "10 Mar 2026",
            "time": "14:00 – 16:00",
            "type": "Consultation",
            "doctor": "Dr. Daniel Chung",
            "department": "Orthopedics",
            "status": "Completed",
            "note": "Pre-op assessment",
            "category": "history",
        },
        {
            "date": "11 Mar 2026",
            "time": "09:00 – 11:00",
            "type": "Surgery",
            "doctor": "Dr. Daniel Chung",
            "department": "Orthopedics",
            "status": "Completed",
            "note": "Tibia fracture fixation",
            "category": "history",
        },
        {
            "date": "18 Mar 2026",
            "time": "09:30 – 10:00",
            "type": "Follow up",
            "doctor": "Dr. Daniel Chung",
            "department": "Orthopedics",
            "status": "Scheduled",
            "note": "Wound check & X-ray",
            "category": "upcoming",
        },
    ]

    # TODO: Replace with medical information from the database/service layer.
    medical_info = {
        "conditions": [
            "Bone Fracture — Left Tibia",
            "Hypertension — Controlled",
        ],
        "allergies": [
            "Penicillin",
            "Aspirin",
            "Shellfish",
            "Dust Mites",
            "Peanuts",
        ],
        "previous_surgeries": [
            "Tibia Fracture Fixation — Mar 2026",
        ],
        "family_history": [
            "Hypertension",
            "Type 2 Diabetes",
        ],
    }

    return render(
        request,
        "patient/dashboard.html",
        {
            "page_title": "Patient Dashboard",
            "breadcrumb": "Patient / Dashboard",
            "patient": patient,
            "health_metrics": health_metrics,
            "blood_pressure": blood_pressure,
            "prescriptions": prescriptions,
            "appointments": appointments,
            "medical_info": medical_info,
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