from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('userinfo.urls')),
    path('admin/', admin.site.urls),
]