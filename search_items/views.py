from django.views.generic import View
from countries.models import Country
from leagues.models import League
from django.http import JsonResponse
from players.models import Player
from teams.models import Team  
from league_team.models import LeaguesTeam
from trophies.models import Trophy  
# Create your views here.

class SearchItemsView(View):
    def get(self, request, query):
        # Process the request and generate the response
        filtered_leagues = League.objects.filter(slug__icontains=query)
        filtered_teams = Team.objects.filter(slug__icontains=query)
        filtered_players = Player.objects.filter(slug__icontains=query)
        filtered_countries = Country.objects.filter(slug__icontains=query)
        filtered_trophies = Trophy.objects.filter(slug__icontains=query)
        leagues_data = [{'name': league.name, 'img': league.img, 'id': league.id} for league in filtered_leagues]
        teams_data = [{'name': team.name, 'img': team.small_img, 'id': team.id} for team in filtered_teams]
        players_data = [{'name': player.name, 'img': player.img, 'id': player.id} for player in filtered_players]
        countries_data = [{'name': country.name, 'img': country.flag, 'id': country.id} for country in filtered_countries]
        trophies_data = [{'name': trophy.name, 'img': trophy.img, 'id': trophy.id} for trophy in filtered_trophies]
        return JsonResponse({"leagues": leagues_data, "teams": teams_data, "players": players_data, "countries": countries_data, "trophies": trophies_data}, safe=False)