from django.urls import path
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from election import views


router = DefaultRouter()
router.register(r'party', views.PartyViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'appoint', views.AppointViewSet)
router.register(r'vote', views.VoteViewSet)
router.register(r'voteall', views.VoteAllViewSet)

urlpatterns = [
    url(r'^login', views.LoginView.as_view()),
    url(r'^', include(router.urls)),
]

urlpatterns += router.urls
