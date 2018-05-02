from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from election import views


router = DefaultRouter()
router.register(r'party', views.PartyViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
