from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('', account, name='account'),
    path('logout/', logout_user, name='logout'),
    path('register/', SingUpView.as_view(), name='register'),
]
