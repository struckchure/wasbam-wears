from django.urls import path

from accounts.api import (
    UserDetailAPI,
    RegisterAPI,
    LoginAPI,
    LogoutAPI
)


app_name = 'accounts'

urlpatterns = [
    path('accounts/', UserDetailAPI.as_view(), name='details'),
    path('accounts/register/', RegisterAPI.as_view(), name='register'),
    path('accounts/login/', LoginAPI.as_view(), name='login'),
    path('accounts/logout/', LogoutAPI.as_view(), name='logout'),
]
