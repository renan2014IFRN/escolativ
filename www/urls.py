from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^alunos/([a-z0-9-]+)/$',views.detalhes, name='detalhes'),
    url(r'^alunos/([a-z0-9-]+)/editar/$',views.editar, name='editar'),
    
]