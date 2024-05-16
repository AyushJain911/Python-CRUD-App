from django.urls import path
from newapp import views

urlpatterns = [
    path("hello/", views.hello, name="hello"),
    path("users_list/",views.users_list, name="users_list"),
    path("new_user/",views.new_user, name="new_user"),
    path('users/<int:user_id>/', views.user_details, name='user_details'),
    path('users/delete/<int:user_id>/', views.delete_user, name='delete_user'),
]