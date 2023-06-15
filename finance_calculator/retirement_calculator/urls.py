from django.urls import path
from . import views

app_name = 'retirement_calculator'

urlpatterns = [
    path('', views.retirement_calulator)
]