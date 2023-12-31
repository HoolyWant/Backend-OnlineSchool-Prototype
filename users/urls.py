from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .apps import UsersConfig
from .views import MyTokenObtainPairView, UserRetrieveApi

app_name = UsersConfig.name

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/<int:pk>', UserRetrieveApi.as_view(), name='пользователь'),
]

