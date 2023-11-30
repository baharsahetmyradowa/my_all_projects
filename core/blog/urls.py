from . import views 
from django.urls import path

urlpatterns = [
    path("",views.ShowPost.as_view()),
]
