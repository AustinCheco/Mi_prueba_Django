from django.conf.urls import url, include

from apps.registro.views import index

urlpatterns = [
   url(r'^$', index),
  
]