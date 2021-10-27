from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chainstore/<int:chainstore_id>', views.chainstore_by_id, name='chainstore_by_id')
]