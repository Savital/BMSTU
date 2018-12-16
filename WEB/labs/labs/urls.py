from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^',  include('Intro.urls')),
    url('Intro/',  include('Intro.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)