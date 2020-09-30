from django.urls import path

from . import views

app_name = "breeding"
urlpatterns = [
    path("", views.index, name="index"),
    path("falcons/", views.FalconList.as_view(), name="falcons"),
    path("falcon/add", views.FalconCreate.as_view(), name="falcon-create"),
    path(
        "falcon/addyoung", views.YoungFalconCreate.as_view(), name="young-falcon-create"
    ),
    path("falcon/<int:pk>", views.FalconDetail.as_view(), name="falcon-detail"),
    path("falcon/<int:pk>/update", views.FalconUpdate.as_view(), name="falcon-update"),
    path("falcon/<int:pk>/delete", views.FalconDelete.as_view(), name="falcon-delete"),
    path("pairs/", views.PairList.as_view(), name="pairs"),
    path("pair/add", views.PairCreate.as_view(), name="pair-create"),
    path("pair/<int:pk>", views.PairDetail.as_view(), name="pair-detail"),
    path("pair/<int:pk>/update", views.PairUpdate.as_view(), name="pair-update"),
    path("pair/<int:pk>/delete", views.PairDelete.as_view(), name="pair-delete"),
]
