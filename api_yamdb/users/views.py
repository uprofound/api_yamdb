from rest_framework import viewsets, filters, mixins

from .models import User, UserManager

from .serializers import UserSerializer


class ListRetrieveViewSet(mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    pass


class UserViewSet(ListRetrieveViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
