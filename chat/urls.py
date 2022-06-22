from django.urls import path
from .views import index, detail, sentMessages, chats


urlpatterns = [
    path('', index, name='index'),
    path('message/<int:pk>', detail, name='detail'),
    path('sent_msg/<int:pk>', sentMessages, name='sent_msg'),
    path('chats/', chats, name='chats'),
]