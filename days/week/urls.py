from django.urls import path
from . import views

urlpatterns = [
    path("<int:month>",views.days_number),
    path("<str:month>",views.days_string),
    path("<weeks>/",views.get_templates),
]
