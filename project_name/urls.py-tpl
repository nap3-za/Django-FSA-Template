from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

from core.misc import views as misc_views
from core.apps.account import views as account_views


urlpatterns = [
    # Authentication
    path("sign-up/", account_views.sign_up_view, name="sign-up"),
    path("sign-in/", account_views.sign_in_view, name="sign-in"),

    path("logout/", account_views.logout_view, name="logout"),

    # App url config imports
    path("", include("core.misc.urls", namespace="misc")),
    path("account/", include("core.apps.account.urls", namespace="account")),
    
    # Project-specific views aka Miscellaneous views
    path("", misc_views.home_view, name="home"),
    path("dashboard/", misc_views.dashboard_view, name="dashboard"),

    path('500/', misc_views.server_error_view, name="500"),
    path('404/', misc_views.page_not_found_view, name="404"),
    path('403/', misc_views.perm_denied_view, name="403"),

    path("admin/", admin.site.urls),

    # Password related views using default views
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name="account/password-reset/reset.html"), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="account/password-reset/reset_done.html"), name="password_reset_done"),
    path("password-reset/complete/", auth_views.PasswordResetCompleteView.as_view(template_name="account/password-reset/reset_complete.html"), name="password_reset_complete"),    
    path("password-reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="account/password-reset/reset_confirm.html"), name="password_reset_confirm"),

    path("password-change/done/", auth_views.PasswordChangeDoneView.as_view(template_name="account/password-reset/change_done.html"),name="password_change_done"),
    path("password-change/", auth_views.PasswordChangeView.as_view(template_name="account/password-reset/change.html"),name="password_change"),
    path("accounts/login/", account_views.sign_in_view, name="sign-in"), # For redirect purposes by above default views
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
