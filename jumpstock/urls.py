"""jumpstock URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
import authentication.views as authentication_views
from django.conf import settings
from rest_framework_swagger.views import get_swagger_view
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)

schema_view = get_swagger_view(title='Registration')

router = routers.DefaultRouter()
router.register(r'users', authentication_views.UserViewSet)


urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('api/register/', authentication_views.UserCreateAPIView.as_view(), name='register'),
    #path('api/', include('rest_framework.urls', namespace='rest_framework')),
    
    # 
    # path('api/login/', authentication_views.UserLoginAPIView.as_view(), name='login'),
    # path('api/logout', authentication_views.UserLogoutAPIView.as_view(), name='logout'),
    path('authentication/', include('authentication.urls')),
    # path('^api/docs/', schema_view, name='api-doc'),
    
]
