from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

from .forms import EmailConfigForm
from .models import EmailConfig


def email_config_view(request):
    config = EmailConfig.objects.first()

    if request.method == "POST":
        form = EmailConfigForm(request.POST, instance=config)
        if form.is_valid():
            form.save()
            return render(request, "success.html", {"name": "Email Configuration Saved"})
    else:
        form = EmailConfigForm(instance=config)

    return render(request, "email_config.html", {"form": form})


def load_email_settings():
    config = EmailConfig.objects.first()
    if not config:
        return False

    settings.EMAIL_HOST = config.email_host
    settings.EMAIL_PORT = config.email_port
    settings.EMAIL_HOST_USER = config.email_host_user
    settings.EMAIL_HOST_PASSWORD = config.email_host_password
    settings.EMAIL_USE_TLS = config.email_use_tls
    settings.EMAIL_USE_SSL = config.email_use_ssl
    return True


def send_test_email(request):
    if not load_email_settings():
        return HttpResponse("No email configuration found.")

    try:
        recipient = settings.TEST_EMAIL_RECIPIENT or settings.EMAIL_HOST_USER
        send_mail(
            subject="Test Email",
            message="This is a test email from Django.",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[recipient],
            fail_silently=False,
        )
        return HttpResponse("Email sent successfully.")
    except Exception as exc:
        return HttpResponse(f"Error: {exc}")
