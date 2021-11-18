from rest_framework import generics
from parqueadero.models.manageUser import modelUser
from parqueadero.serializers.userSerializer import LoginResgistro_serializer

class getUser(generics.RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        self.queryset= modelUser.objects.all()
        self.serializer_class = LoginResgistro_serializer
        return super().get(request, *args, **kwargs)

class updateUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = modelUser.objects.all()
    serializer_class   = LoginResgistro_serializer
    
    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

class DeleteUser(generics.DestroyAPIView):
    queryset           = modelUser.objects.all()
    serializer_class   = LoginResgistro_serializer
    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)