from django.urls import path

from accounts.api import (
    RegisterAPI,
    LoginAPI,
    LogoutAPI
)


app_name = 'accounts'

urlpatterns = [
    path('accounts/register/', RegisterAPI.as_view(), name='register'),
    path('accounts/login/', LoginAPI.as_view(), name='login'),
    path('accounts/logout/', LogoutAPI.as_view(), name='logout'),
]
