from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import ListView
from countries.models import Country
from leagues.models import League
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

        player = get_object_or_404(Player, pk=pk)
        related_country = Country.objects.filter(pk=player.id_country_id).first()
        related_team = Team.objects.filter(pk=player.id_team_id).first()
        
        team_pk = kwargs.get('team_pk')
        league_pk = kwargs.get('league_pk')
        country_pk = kwargs.get('country_pk')

        if team_pk:
            team = get_object_or_404(Team, pk=team_pk)

        if league_pk:
            league = get_object_or_404(League, pk=league_pk)

        if country_pk:
            country = get_object_or_404(Country, pk=country_pk)
        
        breadcrumbs = []

        if league_pk or team_pk or country_pk:
            if country_pk:
                breadcrumbs += [
                    {'url': f"/countries/", 'name': "Países"},
                    {'url': f"/countries/{country.id}", 'name': country.name}
                ]
                
                if league_pk:
                    breadcrumbs += [
                        {'url': f"/countries/{country.id}/leagues/{league.id}", 'name': league.name}
                    ] 
                    
                    if team_pk:
                        breadcrumbs += [
                            {'url': f"/countries/{country.id}/leagues/{league.id}/teams/{team.id}", 'name': team.name}
                        ] 
                        
                if team_pk and not league_pk:
                    breadcrumbs += [
                        {'url': f"/countries/{country.id}/teams/{team.id}", 'name': team.name}
                    ] 
                
            elif league_pk:
                breadcrumbs += [
                    {'url': f"/leagues/", 'name': "Ligas"},
                    {'url': f"/leagues/{league.id}", 'name': league.name}
                ]
                if team_pk:
                    breadcrumbs += [
                        {'url': f"/teams/{team.id}", 'name': team.name}
                    ] 
                    
            elif team_pk and not league_pk:
                breadcrumbs += [
                    {'url': f"/teams/", 'name': "Equipes"},
                    {'url': f"/teams/{team.id}", 'name': team.name}
                ]

                    
            breadcrumbs += [
                {'url': "", 'name': player.name}
            ]
            
            
        else:
            breadcrumbs += [
                {'url': f"/players/", 'name': 'Jogadores'},
                {'url': "", 'name': player.name}
            ]        

        context = {
            'player': player,
            'breadcrumbs': breadcrumbs,
            'related_country': related_country,
            'related_team': related_team,
        }

        return render(request, self.template_name, context)
