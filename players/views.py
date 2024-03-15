from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import ListView
from countries.models import Country
from players.models import Player
from teams.models import Team

# Create your views here.
def order_list(list=[], key="", order=""):
    if key:
        list = list.order_by(f"{order}{key}")
    return list


class PlayerListView(ListView):
    model = Player
    paginate_by = 50  

    def get_queryset(self):
        queryset = super().get_queryset()

        order_by_param = self.request.GET.get('field', 'value_market')
        order_dir_param = self.request.GET.get('order', 'desc')  
        if order_dir_param == 'desc':
            queryset = order_list(queryset, order_by_param, "-")
        else:
            queryset = order_list(queryset, order_by_param, "")

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context





class PlayerInfoView(View):
    model = Team
    template_name = 'players/player_detail.html'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')

        print("PK: ", pk)
        player = get_object_or_404(Player, pk=pk)
        related_country = Country.objects.filter(pk=player.id_country_id).first()
        related_team = Team.objects.filter(pk=player.id_team_id).first()

        context = {
            'player': player,
            'related_country': related_country,
            'related_team': related_team,
        }

        return render(request, self.template_name, context)
