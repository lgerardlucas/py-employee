from django.urls import include, path

from rest_framework import routers
from register.api.viewsets import RegisterViewSet

api_router = routers.DefaultRouter()
api_router.register("", RegisterViewSet)

urlpatterns = [
    path('list/', include(api_router.urls)),
    path('create/', include(api_router.urls)),
    path('update/', include(api_router.urls)),
    path('delete/', include(api_router.urls)),
]
