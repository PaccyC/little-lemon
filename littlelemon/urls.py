
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/",include("littleLemonAPI.urls")),
    path("auth/",include("djoser.urls")),
    path("auth/",include("djoser.urls.authtoken")),
    path("",include('myapp.urls'))
]
