from django.urls import path
from . import views
from .views import signup_view, UserDeleteView, ExpenseListCreate,ExpenseRetrieveUpdateDestroy
from django.contrib.auth import views as auth_views

app_name = "polls"
urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("index", views.Index.as_view(), name="index"),
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
    path('signup/', signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='polls/login.html'), name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("dashboard/", views.UserDashboardView.as_view(), name="user_dashboard"),
    path('delete_account/', UserDeleteView.as_view(), name='delete_account'),
    path('api/expenses/', ExpenseListCreate.as_view(), name='expense-list-create'),
    path('api/expenses/<int:pk>/', ExpenseRetrieveUpdateDestroy.as_view(), name='expense-retrieve-update-destroy'),
]