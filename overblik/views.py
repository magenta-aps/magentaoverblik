from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.views.generic import TemplateView
from overblik.models import Server


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        if 'servers' not in kwargs:
            kwargs['servers'] = Server.objects.all()
        return kwargs
