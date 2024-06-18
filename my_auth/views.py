from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from clientuser.serializer import AuthSerializer
from .models import Auth
from rest_framework import serializers
from rest_framework_simplejwt.tokens import AccessToken



class UserDetailsSerializer(serializers.Serializer):
    user = AuthSerializer()


class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserDetailsSerializer({'user': user})
        print(serializer.data)
        return Response(serializer.data)