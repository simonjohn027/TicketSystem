from django.views.generic import RedirectView
from django.contrib.auth.views import LogoutView
from accounts.views import LoginView, RegisterView
from django.contrib import admin
from django.urls import path, re_path,include

urlpatterns = [
    path("", include("ticket.urls")),
    re_path(r'^accounts/$', RedirectView.as_view(url='/account')),
    path('account/', include("accounts.urls")),
    path('accounts/', include("accounts.password.urls")),
    re_path(r'^register/$', RegisterView.as_view(), name='register'),
    re_path(r'^login/$', LoginView.as_view(), name='login'),
    re_path(r'^logout/$', LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]
