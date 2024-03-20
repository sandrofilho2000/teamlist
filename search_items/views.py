from countries.models import Country
from leagues.models import League
from django.http import JsonResponse
from players.models import Player
from stadiums.models import Stadium
from teams.models import Team  
from trophies.models import Trophy  
from django.views.generic import ListView, View
from countries.models import Country

class SearchItemsView(View):
    def get(self, request, query):
        # Process the request and generate the response
        filtered_leagues = League.objects.filter(slug__icontains=query)[:10]
        filtered_teams = Team.objects.filter(slug__icontains=query)[:10]
        filtered_players = Player.objects.filter(slug__icontains=query)[:10]
        filtered_countries = Country.objects.filter(slug__icontains=query)[:10]
        filtered_trophies = Trophy.objects.filter(slug__icontains=query)[:10]
        filtered_stadiums = Stadium.objects.filter(slug__icontains=query)[:10]
        
        leagues_data = [{'name': league.name, 'img': league.img, 'id': league.id} for league in filtered_leagues]
        teams_data = [{'name': team.name, 'img': team.img, 'id': team.id} for team in filtered_teams]
        players_data = [{'name': player.name, 'img': player.img, 'id': player.id} for player in filtered_players]
        countries_data = [{'name': country.name, 'img': country.flag, 'id': country.id} for country in filtered_countries]
        trophies_data = [{'name': trophy.name, 'img': trophy.img, 'id': trophy.id} for trophy in filtered_trophies]
        stadiums_data = [{'name': stadium.name, 'imgs': stadium.imgs, 'id': stadium.id} for stadium in filtered_stadiums]
        return JsonResponse({"leagues": leagues_data, "teams": teams_data, "players": players_data, "countries": countries_data, "trophies": trophies_data, "stadiums": stadiums_data}, safe=False)
    
class SearchView(ListView):
    template_name = 'search_items/search_items_list.html'
    context_object_name = 'search_results'
    paginate_by = 30
    
    def get_queryset(self):
        table = self.kwargs.get('table')
        query = self.kwargs.get('query')
        
        if table == 'players':
            queryset = Player.objects.filter(slug__icontains=query)
        elif table == 'countries':
            queryset = Country.objects.filter(slug__icontains=query)
        elif table == 'leagues':
            queryset = League.objects.filter(slug__icontains=query)
        elif table == 'teams':
            queryset = Team.objects.filter(slug__icontains=query)
        elif table == 'trophies':
            queryset = Trophy.objects.filter(slug__icontains=query)
        elif table == 'stadiums':
            queryset = Stadium.objects.filter(slug__icontains=query)
        else:
            queryset = []
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table'] = self.kwargs.get('table', '')
        context['query'] = self.kwargs.get('query', '')
        return context