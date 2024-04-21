from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path("notes/", views.NoteListCreate.as_view(), name="note-list"),
    path("notes/delete/<int:pk>/", views.NoteDelete.as_view(), name="delete-note"),
]