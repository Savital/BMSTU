from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static

from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^$',  views.index),
    url(r'intro', views.index),
    url(r'send/', views.send),
    url(r'api/', views.API.as_view()),
    url(r'hello2', views.hello2),
    url(r'hello3', views.hello3),
    url(r'^hello', TemplateView.as_view(template_name='html/Hello.html')),
    url(r'^hack', TemplateView.as_view(template_name='html/hack.txt', content_type='text/plain'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)