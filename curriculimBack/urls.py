from django.contrib import admin
from django.urls import path
from mails.views import send_email

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/send-email/', send_email),
]
