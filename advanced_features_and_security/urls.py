from django.urls import path
from .views import admin_view
from .views import librarian_view
from .views import member_view

urlpatterns = [
    path("admin-role/", admin_view, name="admin_view"),
    path("librarian-role/", librarian_view, name="librarian_view"),
    path("member-role/", member_view, name="member_view"),
]
