from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts.views import UserView, ClientList, ClientCreate, ClientDetail
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = DefaultRouter()
router.register('users', UserView)
router.register('clientlist', ClientList)


urlpatterns = [
    path('', include(router.urls)),
    path('client/create/', ClientCreate.as_view()),
    path('client/detail/', ClientDetail.as_view()),

]



