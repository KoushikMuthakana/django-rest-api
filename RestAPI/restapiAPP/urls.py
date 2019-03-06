from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from django.urls import include

router=DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,base_name='hello-viewset')
router.register('profile',views.UserProfileViewSet)
router.register('login',views.LoginViewSet,base_name='login')

urlpatterns = [

    path('hello-view/',views.HelloAPI.as_view()),
    path('',include(router.urls)),


]
