from django.urls import path

from . import views
from .views import FalconList, FalconDetail

app_name = 'breeding'
urlpatterns = [
    path('', views.index, name='index'),
    path('falcons/', FalconList.as_view(), name='falcons'),
    path('falcon/<int:pk>', FalconDetail.as_view(), name='falcon_detail'),
]