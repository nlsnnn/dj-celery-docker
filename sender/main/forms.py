from django import forms


class MailForm(forms.Form):
    subject = forms.CharField(max_length=100, label='Тема письма')
    message = forms.CharField(widget=forms.Textarea(), label='Текст письма')
    recipient = forms.EmailField()