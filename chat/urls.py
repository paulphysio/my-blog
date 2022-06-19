from django.urls import path
from .views import index, detail, sentMessages


urlpatterns = [
    path('', index, name='index'),
    path('message/<int:pk>', detail, name='detail'),
    path('sent_msg/<int:pk>', sentMessages, name='sent_msg'),
]