from django.views.generic import TemplateView

from uptrader import models as uptrader_models


class MainPageView(TemplateView):
    template_name = 'uptrader/index.html'

    def get_context_data(self, **kwargs):
        # Get all previous data
        context = super().get_context_data(**kwargs)
        # Create your own data
        context['menu_obj'] = uptrader_models.Mainmenu.objects.all()
        return context


class Page1View(TemplateView):
    template_name = 'uptrader/1.html'

    def get_context_data(self, **kwargs):
        # Get all previous data
        context = super().get_context_data(**kwargs)
        # Create your own data
        context['menu_obj'] = uptrader_models.Mainmenu.objects.all()
        return context


class Page2View(TemplateView):
    template_name = 'uptrader/2.html'

    def get_context_data(self, **kwargs):
        # Get all previous data
        context = super().get_context_data(**kwargs)
        # Create your own data
        context['menu_obj'] = uptrader_models.Mainmenu.objects.all()
        return context
