from django.urls import path
from . import views

urlpatterns = [
    path('detail/<str:request_name>', views.viewdetail, name="detail"),
    path('', views.index, name="index"),
]