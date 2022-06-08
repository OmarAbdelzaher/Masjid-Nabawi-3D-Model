from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('masjid_app/',include('masjid_app.urls'))
]
