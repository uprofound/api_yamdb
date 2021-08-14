from django.urls import include, path

from .views import APISignup

urlpatterns = [
    path('v1/auth/signup/', APISignup.as_view()),
    path('v1/auth/', include('djoser.urls')),
    path('v1/auth/', include('djoser.urls.jwt')),
]
