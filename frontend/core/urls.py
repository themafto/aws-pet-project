from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test_rds/', views.test_rds, name='test_rds'),
    path('test_redis/', views.test_redis, name='test_redis'),
]
