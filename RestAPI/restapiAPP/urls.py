from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from django.urls import include

router=DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,base_name='hello-viewset')

urlpatterns = [

    path('hello-view/',views.HelloAPI.as_view()),
    path('',include(router.urls)),


]
