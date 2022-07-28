from django.urls import path
from rest_framework import routers
from .api import UserViewSet
from . import views
from . import api
app_name = 'account'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user_register'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('logout/', views.UserLogoutView.as_view(), name='user_logout'),
    path('verify/', views.UserRegisterVerifyCodeView.as_view(), name='verifyCode'),
]
router = routers.SimpleRouter()
router.register('user', api.UserViewSet)
urlpatterns += router.urls