from django.views.generic import TemplateView

from . import plots

class MetroTable(TemplateView):
    template_name = "templates/plot.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(MetroTable, self).get_context_data(**kwargs)
        context['plot'] = plots.plot_metro_table()
        return context