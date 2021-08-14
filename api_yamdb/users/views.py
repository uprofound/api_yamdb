from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.core.mail import send_mail

from .models import User, UserManager

from .serializers import UserSerializer, EmailSerializer, UserCodeSerializer


class APISignup(APIView):
    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            subject = 'hello'
            message = 'hello'
            send_mail(subject, message, None, [serializer.data['email']])
            User.objects.create(
                email=serializer.data['email'],
                username=serializer.data['username'],
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


