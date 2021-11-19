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
Including another URLconf3
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework     import permissions
from drf_yasg2.views    import get_schema_view
from drf_yasg2          import openapi

from django.contrib     import admin
from django.urls        import path, re_path
from parking_customers  import views as parkingView


schema_view = get_schema_view(
      openapi.Info(
         title="Snippets API",
         default_version='v1',
         description="Test description",
         terms_of_service="https://www.google.com/policies/terms/",
         contact=openapi.Contact(email="contact@snippets.local"),
         license=openapi.License(name="BSD License"),
      ),
      public=True,
      permission_classes=(permissions.AllowAny,),
   )

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    path('admin/', admin.site.urls),
    path('parking/create/',                 parkingView.ParkingCreateView.as_view()), 
    path('parking/<int:pk>/',               parkingView.ParkingDetailView.as_view()),
    path('parking/update/<int:pk>/',        parkingView.ParkingUpdateView.as_view()),
    path('parking/remove/<int:pk>/',        parkingView.UserDeleteView.as_view()),
    path('parking/admin/<int:admin_id>/',   parkingView.ListParkingView.as_view()), 
    path('parking/',                        parkingView.ParkingsView.as_view()),
]