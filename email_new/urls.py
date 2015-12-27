from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.enter_email, name='home'),
    url(r'^submit', views.receive_email_data, name='submit')
]
