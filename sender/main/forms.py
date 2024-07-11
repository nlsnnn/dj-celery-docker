from django import forms
from .models import Subscription


class MailForm(forms.Form):
    subject = forms.CharField(max_length=100, label='Тема письма')
    message = forms.CharField(widget=forms.Textarea(), label='Текст письма')
    recipient = forms.EmailField()


class SubscriptionRegisterForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = "__all__"


class SubscriptionSendingForm(forms.Form):
    subject = forms.CharField(max_length=100, label='Тема письма')
    message = forms.CharField(widget=forms.Textarea(), label='Текст письма')