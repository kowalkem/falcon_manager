from django.urls import path

from . import views
from .views import FalconList

app_name = 'breeding'
urlpatterns = [
    path('', views.index, name='index'),
    path('falcons/', FalconList.as_view(), name='falcons'),
    path('falcon/<int:falcon_id>', views.falcon_detail, name='falcon_detail'),
]