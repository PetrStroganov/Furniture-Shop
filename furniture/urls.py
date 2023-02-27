from django.urls import path
from .views import MainPage, GalleryPage, FurnitureDetailView, FurnitureCreateView

urlpatterns = [
    path('', MainPage.as_view(), name="homepage"),
    path('gallery/', GalleryPage.as_view(), name="gallery"),
    path('furniture/<slug:slug>/', FurnitureDetailView.as_view(), name="furniture-detail"),
    path('furniture/create', FurnitureCreateView.as_view(), name="furniture-create")
]
