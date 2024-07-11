from django.urls import path
from . import views


urlpatterns = [
    path('', views.MainPage.as_view(), name='main'),
    path('subscription/', views.SubscriptionRegister.as_view(), name='subscription'),
    path('subscription/sending/', views.SubscriptionSending.as_view(), name='sub_sending')
]