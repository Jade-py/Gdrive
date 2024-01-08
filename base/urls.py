from django.urls import path
from .views import FolderView, FileView

urlpatterns = [
    path('', FolderView.as_view()),
    path('<str:folder>', FileView.as_view())
]