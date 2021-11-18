from rest_framework import exceptions, serializers, status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend
from django.conf import settings
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.serializers import TokenVerifySerializer

class verifyTokenView(TokenVerifyView):

    def post(self, request, *args, **kwargs):

        serializer_Verify = TokenVerifySerializer(data=request.data)
        token_backend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        
        try:

            serializer_Verify.is_valid(raise_exception=True)
            token_data = token_backend.decode(request.data['token'])
            serializer_Verify.validated_data["UserId"] = token_data['user_id']
        except TokenError as er:
            
            raise InvalidToken(er.args[0])
        except Exception as er:
            print(er)

        return Response(serializer_Verify.validated_data, status=status.HTTP_200_OK)