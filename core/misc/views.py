from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home_view(request):
    return render(request, "misc/home.html")

@login_required(login_url="sign-in")
def dashboard_view(request):
    return render(request, "misc/dashboard.html")

def server_error_view(request):
    return render(request, "misc/error-pages/500.html")

def page_not_found_view(request):
    return render(request, "misc/error-pages/404.html")

def perm_denied_view(request):
    return render(request, "misc/error-pages/403.html")