from django.urls import path
from .views import UserActionView

urlpatterns = [
    path('log-action/', UserActionView.as_view(), name='log_action'),
]
