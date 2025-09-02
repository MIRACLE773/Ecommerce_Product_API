from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.permissions import AllowAny  # ← add this
from .serializers import LoginSerializer, RegisterSerializer


# Register API
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny] 
    authentication_classes = []  # ← add this`

# Login API
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})  # ← here you return the token
        return Response({"error": "Invalid credentials"}, status=400)
