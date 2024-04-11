from django.contrib import admin
from django.urls import path, include
from API.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", TodosListMixinApiView.as_view()),
    path("todo/<pk>", TodosDetailMixinApiView.as_view()),
    path("users", TodosGenericApiView.as_view()),

    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    path('api-auth/', include('rest_framework.urls'))
]
