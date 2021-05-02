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
    path("offices/", views.OfficeList.as_view(), name="offices"),
    path("office/add", views.OfficeCreate.as_view(), name="office-create"),
    path("office/<int:pk>", views.OfficeDetail.as_view(), name="office-detail"),
    path("office/<int:pk>/update", views.OfficeUpdate.as_view(), name="office-update"),
    path("office/<int:pk>/delete", views.OfficeDelete.as_view(), name="office-delete"),
    path("docs", views.DocList.as_view(), name="docs"),
    path("doc/add", views.DocCreate.as_view(), name="doc-create"),
    path("birth_certs/", views.Birth_certList.as_view(), name="birth_certs"),
    path("birth_cert/add", views.Birth_certCreate.as_view(), name="birth_cert-create"),
    path(
        "birth_cert/<int:pk>",
        views.Birth_certDetail.as_view(),
        name="birth_cert-detail",
    ),
    path("birth_cert/<int:pk>/update", views.Birth_certUpdate.as_view(), name="birth_cert-update"),
    path("birth_cert/<int:pk>/delete", views.Birth_certDelete.as_view(), name="birth_cert-delete"),
]
