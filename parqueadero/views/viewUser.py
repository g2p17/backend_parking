from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.views import APIView
from parqueadero.serializers.userSerializer import LoginResgistro_serializer
from parqueadero.models import modelUser


class RegisterView(APIView):

    def post(self, request,*args,**kwargs):
        serializer = LoginResgistro_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        token_data = {"email":request.data['email'],
        "password":request.data["password"]}

        try:
            tokenSerializer = TokenObtainPairSerializer(data=token_data)
            tokenSerializer.is_valid(raise_exception=True)
            return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response('Error in token generation', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request,*args,**kwargs):

        arrayUsers = modelUser.objects.all()
        serializer_object = LoginResgistro_serializer(arrayUsers, many=True)
        
        return Response(serializer_object.data)