from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Furniture

class MainPage(TemplateView):
    template_name = "furniture/main.html"


class GalleryPage(ListView):
    template_name = "furniture/gallery.html"
    model = Furniture
    context_object_name = "furnitures"


class FurnitureDetailView(DetailView):
    model = Furniture
    context_object_name = "furniture"
    template_name = "furniture/furniture-detail.html"