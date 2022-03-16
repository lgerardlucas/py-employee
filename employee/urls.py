from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('api/', include('register.urls')),
    path('', admin.site.urls),
]
