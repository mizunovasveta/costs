from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("<int:pk>/", views.Detail.as_view(), name="detail"),
    path("<int:pk>/update/", views.Update.as_view(), name="update"),
    path("create/", views.Create.as_view(), name="create"),
    path("<int:pk>/delete/", views.Delete.as_view(), name="delete"),
    path("create_category/", views.Create_category.as_view(), name="create_category"),
]