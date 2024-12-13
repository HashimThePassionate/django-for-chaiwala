from django.shortcuts import render
from typing import Any
from django.views.generic import TemplateView
# Create your views here.



class HomePageView(TemplateView):
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["page"] = 'Chaiwala Patti Page'
        return context
    
    template_name = "home.html"
class AboutPageView(TemplateView):
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["name"] = 'Kashan Shafeeq'
        context["age"] = 22
        return context
    template_name = "about.html"
