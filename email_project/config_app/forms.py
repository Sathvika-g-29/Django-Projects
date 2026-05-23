from django import forms
from .models import EmailConfig

class EmailConfigForm(forms.ModelForm):
    class Meta:
        model = EmailConfig
        fields = [
            "email_host",
            "email_port",
            "email_host_user",
            "email_host_password",
            'email_use_tls',
            'email_use_ssl',
        ]
        widgets = {
            "email_host_password": forms.PasswordInput(),
        }
