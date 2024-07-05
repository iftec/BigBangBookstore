from django.shortcuts import render
from django.views import generic


class StoreFront(generic.TemplateView):
    template_name = "storefront.html"
