from typing import Any
from django.http import HttpRequest, HttpResponse
from django.views.generic import FormView
from django.urls import reverse

from .forms import MailForm
from .tasks import send


class MainPage(FormView):
    form_class = MailForm
    template_name = 'main/index.html'

    def get_success_url(self) -> str:
        return reverse('main')

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        data = request.POST
        send.delay(data)
        print('OK')
        return super().post(request, *args, **kwargs)
