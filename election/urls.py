from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from election import views


router = DefaultRouter()
router.register(r'party', views.PartyViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^register/$', views.CreateUserView.as_view()),
    url(r'^appoint/$', views.AppointView.as_view()),
]
