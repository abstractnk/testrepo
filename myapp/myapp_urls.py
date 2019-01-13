from django.urls import path
from .views import *
from django.views.generic import TemplateView


urlpatterns = [
	path('hello/<str:name>/', hello),
	path('time/', time),
	path('crud/', crudops),
	path('send/<str:emailto>/', sendSimpleEmail),
	path('login/', login, name='login'),
	path('signin/', TemplateView.as_view(template_name = 'myapp/login.html')),
]
