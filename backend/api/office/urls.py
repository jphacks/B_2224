
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
#from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('five.urls')),
]
