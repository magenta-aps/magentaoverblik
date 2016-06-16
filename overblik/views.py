from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.views.generic import TemplateView
from overblik.models import Server, Customer, HostingProvider, Solution


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servers'] = Server.objects.all()
        context['customers'] = Customer.objects.all()
        context['hosting_providers'] = HostingProvider.objects.all()
        context['solutions'] = Solution.objects.all()

        return context
