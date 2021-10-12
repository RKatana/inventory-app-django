from django.contrib.auth import get_user_model
from django.urls import path
from rest_framework.generics import ListCreateAPIView
from .views import MyObtainTokenPairView
from rest_framework_simplejwt.views import TokenRefreshView
from .serializers import UserSerializer
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Registration')

urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh', TokenRefreshView.as_view(), name='token_refresher'),
    path('users/', ListCreateAPIView.as_view(queryset=get_user_model().objects.all(), serializer_class=UserSerializer)),
    

]