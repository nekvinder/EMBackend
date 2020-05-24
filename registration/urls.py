from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('registration',views.RegistrationView)
router.register('IdCard',views.IdCardView)
router.register('Group',views.GroupView)
router.register('Login',views.LoginView)


urlpatterns = [
    path('',include(router.urls))
]