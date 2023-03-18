from django.contrib import admin
from django.urls import path, include
from account.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('', MainHome, name='main_str')
]
