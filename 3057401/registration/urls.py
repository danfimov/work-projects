from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^create/$', views.order_create, name='order_create'),
]