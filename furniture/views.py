from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import Furniture
from transliterate import translit

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


class FurnitureCreateView(CreateView):
    template_name = "furniture/furniture-create.html"
    model = Furniture
    fields = ["title", "description", "price", "type", "image"]
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.slug = translit(form.instance.title.replace(" ", "_"), "ru", reversed=True) #TODO: добавить уникальность
        return super().form_valid(form)