"""parking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



from parqueadero import views
from parqueadero.views.viewUser import RegisterView
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',RegisterView.as_view()),
    path('login/',TokenObtainPairView.as_view()),
    path('refresh/',TokenRefreshView.as_view()),
    path('verifyToken/', views.verifyTokenView.as_view()),
    path('estaciones/', views.viewEstacion.as_view()),
    path('getuser/<int:pk>/', views.getUser.as_view()),
    path('update/<int:pk>/', views.updateUser.as_view()),
    path('deleteUser/<int:pk>/', views.DeleteUser.as_view()),
    path('getestacion/<str:pk>/', views.getEstacion.as_view()),
    path('delestacion/<str:pk>/', views.DeleteEstacion.as_view()),
    path('upestacion/<str:pk>/',views.updateEstacion.as_view()),
    path('reservas/', views.viewReservas.as_view()),
    path('delreservas/<int:pk>/',views.DeleteReserva.as_view()),
    path('upreserva/<int:pk>/',views.updateReserva.as_view()),
    path('getreserva/<int:pk>/',views.getReserva.as_view())
]
