from django.urls import include, path


urlpatterns = [
    path('v1/auth/signup/', include('djoser.urls')),
    path('v1/auth/token/', include('djoser.urls.jwt')),
]
