from django.urls import path

from . import views

app_name = "breeding"
urlpatterns = [
    path("", views.index, name="index"),
    path("falcons/", views.FalconList.as_view(), name="falcons"),
    path("falcon/add", views.FalconCreate.as_view(), name="falcon-create"),
    path(
        "falcon/addyoung/<int:pair_pk>",
        views.YoungFalconCreate.as_view(),
        name="young-falcon-create",
    ),
    path("falcon/<int:pk>", views.FalconDetail.as_view(), name="falcon-detail"),
    path("falcon/<int:pk>/update", views.FalconUpdate.as_view(), name="falcon-update"),
    path("falcon/<int:pk>/delete", views.FalconDelete.as_view(), name="falcon-delete"),
    path("pairs/", views.PairList.as_view(), name="pairs"),
    path("pair/add", views.PairCreate.as_view(), name="pair-create"),
    path("pair/<int:pk>", views.PairDetail.as_view(), name="pair-detail"),
    path("pair/<int:pk>/update", views.PairUpdate.as_view(), name="pair-update"),
    path("pair/<int:pk>/delete", views.PairDelete.as_view(), name="pair-delete"),
    path("aviaries/", views.AviaryList.as_view(), name="aviaries"),
    path("aviary/add", views.AviaryCreate.as_view(), name="aviary-create"),
    path("aviary/<int:pk>", views.AviaryDetail.as_view(), name="aviary-detail"),
    path("aviary/<int:pk>/update", views.AviaryUpdate.as_view(), name="aviary-update"),
    path("aviary/<int:pk>/delete", views.AviaryDelete.as_view(), name="aviary-delete"),
    path("docs", views.Docs.as_view(), name="docs"),
    path("birth_cert", views.Birth_certCreate.as_view(), name="birth_cert-create"),
    path(
        "birth_cert/<int:pk>",
        views.Birth_certDetail.as_view(),
        name="birth_cert-detail",
    ),
]
