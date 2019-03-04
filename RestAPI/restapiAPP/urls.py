from django.urls import path
from . import views

urlpatterns = [

    path('hello-view/',views.HelloAPI.as_view()),


]
