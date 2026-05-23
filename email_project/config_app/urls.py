from django.urls import path
from .views import email_config_view, send_test_email

urlpatterns = [
    path("email-config/", email_config_view, name="email_config"),
    path("send-test/", send_test_email, name="send_test"),
]