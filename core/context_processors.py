from .navigation import (
    get_admin_navigation,
    get_doctor_navigation,
    get_patient_navigation,
)


def dashboard_navigation(request):
    """
    Provides role-specific dashboard navigation to all templates.
    """

    if not request.user.is_authenticated:
        return {
            
            "sidebar_items": get_patient_navigation(),
        }

    # if not request.user.is_authenticated:
    # return {
    #     "sidebar_items": [],
    # }

    # Temporary role detection.
    # Replace this later with your actual User/Profile role system.
    if request.user.is_staff:
        navigation = get_admin_navigation()

    elif hasattr(request.user, "doctor_profile"):
        navigation = get_doctor_navigation()

    else:
        navigation = get_patient_navigation()

    return {
        "sidebar_items": navigation,
    }