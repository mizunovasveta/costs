from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("<int:pk>/", views.Detail.as_view(), name="detail"),
    path("<int:pk>/update/", views.Update.as_view(), name="update"),
]