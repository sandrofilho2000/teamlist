from django.shortcuts import render
from django.views.generic import ListView
from team_trophy.models import TeamTrophy
from trophies.models import Trophy

# Function to order a list by a specified key and order
def order_list(queryset, key="", order=""):
    if key:
        return queryset.order_by(f"{order}{key}")
    return queryset

class TrophyListView(ListView):
    model = TeamTrophy
    paginate_by = 50  

    # Get queryset based on user input parameters for ordering
    def get_queryset(self):
        queryset = super().get_queryset()

        order_by_param = self.request.GET.get('field', 'id_trophy__name')
        order_dir_param = self.request.GET.get('order', 'desc')  
        if order_dir_param == 'desc':
            queryset = order_list(queryset, order_by_param, "-")
        else:
            queryset = order_list(queryset, order_by_param, "")

        return queryset

    # Get context data for the view
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
