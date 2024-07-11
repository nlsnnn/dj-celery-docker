from typing import Any
from django.http import HttpRequest, HttpResponse
from django.views.generic import FormView
from django.urls import reverse

from .forms import MailForm, SubscriptionRegisterForm, SubscriptionSendingForm
from .tasks import send, subscription_register, subscription_sending
from .models import Subscription


class MainPage(FormView):
    form_class = MailForm
    template_name = 'main/index.html'

    def get_success_url(self) -> str:
        return reverse('main')

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        data = request.POST
        send.delay(data)
        return super().post(request, *args, **kwargs)


class SubscriptionRegister(FormView):
    form_class = SubscriptionRegisterForm
    template_name = 'main/subscription.html'

    def form_valid(self, form: Any) -> HttpResponse:
        form.save()
        subscription_register.delay(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse('main')


class SubscriptionSending(FormView):
    form_class = SubscriptionSendingForm
    template_name = 'main/subscription.html'

    def get_success_url(self) -> str:
        return reverse('main')

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        data = request.POST
        emails = [obj.email for obj in Subscription.objects.all()]
        subscription_sending.delay(data, emails)
        return super().post(request, *args, **kwargs)