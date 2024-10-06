from django import forms
from clothes.models import Contact
from captcha.fields import CaptchaField


class ContactForm(forms.ModelForm):
    captcha = CaptchaField()  # captcha for contact form

    class Meta:
        model = Contact
        fields = '__all__'
