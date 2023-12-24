from django.urls import path
from . import views

urlpatterns = [
    path('', views.getComments),
    path('create', views.addComment),
    path('read/<str:pk>', views.getComment),
    path('update/<str:pk>', views.updateComment),
    path('delete/<str:pk>', views.deleteComment),
]