from .views import Registrationview
from django.urls import path



urlpatterns = [
    path('register',Registrationview.as_view(),name="register")
]