from django.urls import include, path

# from rest_framework.routers import DefaultRouter

from .views import APISignup

# router = DefaultRouter()
# router.register('auth/signup/', APISignup.as_view(), basename='signup')

urlpatterns = [
    path('v1/auth/signup/', APISignup.as_view()),
    path('v1/auth/', include('djoser.urls')),
    path('v1/auth/', include('djoser.urls.jwt')),
]

