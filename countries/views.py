from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from countries.models import Country
from .models import CountryColorForm
from leagues.models import League
from teams.models import Team
from players.models import Player

# Helper function to order a queryset based on a specified key and order
def order_list(queryset, key="", order=""):
    if key:
        return queryset.order_by(f"{order}{key}")
    return queryset

# View for listing countries
class CountryListView(ListView):
    model = Country
    paginate_by = 20  

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(num_teams=Count('team', distinct=True))
        queryset = queryset.annotate(num_leagues=Count('league', distinct=True))
        order_by_param = self.request.GET.get('field')
        order_dir_param = self.request.GET.get('order', 'asc')  
        if order_dir_param == 'desc':
            queryset = order_list(queryset, order_by_param, "-")
        else:
            queryset = order_list(queryset, order_by_param, "")
        return queryset

# View for displaying details of a specific country
class CountryDetailView(ListView):
    template_name = 'countries/country_detail.html'  

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')  
        country = get_object_or_404(Country, pk=pk) 

        # Retrieve leagues related to the country
        order_by_param_league = self.request.GET.get('field_league', 'name')
        order_dir_param_league = self.request.GET.get('order_league', '')
        if order_dir_param_league == "desc":
            order_dir_param_league = "-"
        else:
            order_dir_param_league = ""
        order_league = order_dir_param_league + order_by_param_league
        leagues = League.objects.filter(id_country_id=pk).order_by(order_league)
        top_league = leagues.first()

        # Retrieve teams related to the country
        order_by_param_team = self.request.GET.get('field_team', '-average_market_value')
        order_dir_param_team = self.request.GET.get('order_team', '')
        if order_dir_param_team == "desc":
            order_dir_param_team = "-"
        else:
            order_dir_param_team = ""
        order_team = order_dir_param_team + order_by_param_team
        teams = Team.objects.filter(id_country_id=pk).order_by(order_team)
        top_team = teams.first()

        # Retrieve players related to the country
        order_by_param_player = self.request.GET.get('field_player', '-value_market')
        order_dir_param_player = self.request.GET.get('order_player', '')
        if order_dir_param_player == "desc":
            order_dir_param_player = "-"
        else:
            order_dir_param_player = ""
        order_player = order_dir_param_player + order_by_param_player
        players = Player.objects.filter(id_country_id=pk).order_by(order_player)
        top_players = Player.objects.filter(id_team__id_country_id=pk).order_by("-value_market")[:3]

        # Form for updating country colors
        form = CountryColorForm(instance=country)
                   
        # URL for country flag image
        image_name = f"{country.slug}{country.id}.webp"
        country_flag = f"https://teamlist-bkt-1.s3.amazonaws.com/images/countries/{image_name}"  

        # Pagination for leagues, teams, and players
        page = request.GET.get('page')
        paginator_leagues = Paginator(leagues, 10) 
        paginator_teams = Paginator(teams, 10) 
        paginator_players = Paginator(players, 10) 
        
        try:
            leagues = paginator_leagues.page(page)
        except PageNotAnInteger:
            leagues = paginator_leagues.page(1)
        except EmptyPage:
            leagues = paginator_leagues.page(paginator_leagues.num_pages)
            
        try:
            teams = paginator_teams.page(page)
        except PageNotAnInteger:
            teams = paginator_teams.page(1)
        except EmptyPage:
            teams = paginator_teams.page(paginator_teams.num_pages)
        
        try:
            players = paginator_players.page(page)
        except PageNotAnInteger:
            players = paginator_players.page(1)
        except EmptyPage:
            players = paginator_players.page(paginator_players.num_pages)
            
        # Breadcrumbs for navigation
        breadcrumbs = [
            {'url': f"/countries/", 'name': "Países"},
            {'url': f"", 'name': country.name}
        ]
        
        context = {
            'country': country,
            'main_item': country,
            'main_item_admin': f"/admin/countries/country/{country.pk}/change/",
            'leagues': leagues,
            'top_league': top_league,
            'country_flag': country_flag,
            'players': players,
            'breadcrumbs': breadcrumbs,
            'top_players': top_players,
            'teams': teams,
            'top_team': top_team,
            'paginator_leagues': paginator_leagues,
            'paginator_teams': paginator_teams,
            'paginator_players': paginator_players,
            'form': form
        }
                
        return render(request, self.template_name, context )

    # Handle form submission for updating country colors
    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        country = get_object_or_404(Country, pk=pk)
        form = CountryColorForm(request.POST, instance=country)
        if form.is_valid():
            form.save()
            return redirect('country_detail', pk=pk)  
        context = {
            'country': country,
            'form': form,
        }
        return render(request, self.template_name, context)
