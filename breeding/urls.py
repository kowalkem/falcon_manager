from django.urls import path

from . import views

app_name = 'breeding'
urlpatterns = [
    path('', views.index, name='index'),
    path('falcons/', views.FalconList.as_view(), name='falcons'),
    path('falcon/add', views.FalconCreate.as_view(), name='falcon-create'),
    path('falcon/<int:pk>', views.FalconDetail.as_view(), name='falcon-detail'),
]
