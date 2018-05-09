from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from election import views


router = DefaultRouter()
router.register(r'party', views.PartyViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'appoint', views.AppointViewSet)
router.register(r'vote', views.VoteViewSet)
router.register(r'unvote', views.UnvoteViewSet)
router.register(r'voteall', views.VoteAllViewSet)
router.register(r'castvote', views.CastVoteViewSet)

urlpatterns = [
    url(r'^login', views.LoginView.as_view()),
    url(r'^result', views.ResultView.as_view()),
    url(r'^logout', views.LogoutView.as_view()),
    url(r'^', include(router.urls)),
    url(r'^api-token-auth/', obtain_auth_token),
]

urlpatterns += router.urls
