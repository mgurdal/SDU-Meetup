from django.views.generic.base import TemplateView

class Main(TemplateView):
    template_name = "index.html"

class Dashboard(TemplateView):
    template_name = "dashboard/index.html"