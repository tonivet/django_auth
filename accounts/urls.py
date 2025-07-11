from django.urls import path

from . import views


urlpatterns = [
    path("signup/", views.create_user, name="signup"),
    path("profile/", views.Profile.as_view(), name="profile"),
    path("edit_profile/", views.UserEditView.as_view(), name="edit-profile"),
    path("delete_profile/", views.delete_user, name="delete-profile"),
]


