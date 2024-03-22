from django.urls import path
from . import views
from .views import update_currencies,signup_view
from django.contrib.auth.views import LoginView, LogoutView

app_name = "polls"
urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("<int:pk>/", views.Detail.as_view(), name="detail"),
    path("<int:pk>/update/", views.Update.as_view(), name="update"),
    path("create/", views.Create.as_view(), name="create"),
    path("<int:pk>/delete/", views.Delete.as_view(), name="delete"),
    path("create_category/", views.Create_category.as_view(), name="create_category"),
    path("<int:pk>/update_category/", views.Update_category.as_view(), name="update_category"),
    path("<int:pk>/delete_category/", views.Delete_category.as_view(), name="delete_category"),
    path("index_category/", views.Index_category.as_view(), name="index_category"),
    path("<int:pk>/detail_category/", views.Detail_category.as_view(), name="detail_category"),
    path("create_currency/", views.Create_currency.as_view(), name="create_currency"),
    path('update-currencies/', update_currencies, name='update-currencies'),
    path('signup/', signup_view, name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]