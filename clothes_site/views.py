from django.shortcuts import render


# Maintenance view for all requests
def maintenance_view(request, exception=None):
    return render(request, "maintenance.html", status=503)  # 503 is for service unavailable

