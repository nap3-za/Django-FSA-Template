from django.urls import path
from . import views


app_name="account"

urlpatterns = [
    path("<str:subject_username>/details/", views.details_view, name="details"),
    path("delete-account/", views.delete_account_view, name="delete-account"),
]