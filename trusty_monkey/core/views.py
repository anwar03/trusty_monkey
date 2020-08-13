# from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from rest_framework.views import APIView

# class IndexTemplateView(LoginRequiredMixin, TemplateView):
class IndexTemplateView(TemplateView):

    def get_template_names(self):
        template_name = "index.html"
        return template_name

class DummyView(APIView):
    pass

    