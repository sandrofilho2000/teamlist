from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Sum
from countries.models import Country
from stadiums.models import Stadium
from .models import Team, TeamColorForm
from leagues.models import League
from league_team.models import LeaguesTeam
from players.models import Player

def order_list(queryset, key="", order=""):
    if key:
        return queryset.order_by(f"{order}{key}")
    return queryset

class TeamListView(ListView):
    model = Team
    paginate_by = 50  

    def get_queryset(self):
        queryset = super().get_queryset()
        order_by_param = self.request.GET.get('field')
        order_dir_param = self.request.GET.get('order', 'asc')
        queryset = queryset.annotate(num_leagues=Count('leagues_teams'))

        if order_dir_param == 'desc':
            queryset = order_list(queryset, order_by_param, "-")
        else:
            queryset = order_list(queryset, order_by_param, "")

        return queryset

class TeamInfoView(View):
    model = League
    template_name = 'teams/team_detail.html'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        league_pk = kwargs.get('league_pk')
        country_pk = kwargs.get('country_pk')

        if league_pk:
            league = get_object_or_404(League, pk=league_pk)

        team = get_object_or_404(Team, pk=pk)
        country = Country.objects.filter(pk=team.id_country_id).first()
        stadium = Stadium.objects.filter(pk=team.id_stadium_id).first()
        form = TeamColorForm(instance=team)
        related_country = Country.objects.filter(pk=team.id_country_id).first()
        page = request.GET.get('page')

        order_dir_param_player = self.request.GET.get('order_player', '')
        if order_dir_param_player == "desc":
            order_player = "-"
        else:
            order_player = ""

        order_by_param_player = self.request.GET.get('field_player', '-value_market')
        order_player += order_by_param_player
        players = Player.objects.filter(id_team_id=pk).order_by(order_player)
        team_players_value = players.aggregate(total_value=Sum('value_market'))['total_value']
        paginator_players = Paginator(players, 10)

        try:
            players = paginator_players.page(page)
        except PageNotAnInteger:
            players = paginator_players.page(1)
        except EmptyPage:
            players = paginator_players.page(paginator_players.num_pages)
            
            
            
            
            
            
            
            
        
        order_by_param_trophy = self.request.GET.get('field_trophy', 'season')
        
        if order_by_param_trophy:
            if order_by_param_trophy == 'name':
                order_by_param_trophy = f"id_trophy__{order_by_param_trophy}"

        order_dir_param_trophy = self.request.GET.get('order_trophy', 'asc')
        if order_dir_param_trophy == "desc":
            order_trophy = "-"
        else:
            order_trophy = ""
            
        order_trophy += order_by_param_trophy
        trophies = team.team_trophy.all().order_by(order_trophy)

        paginator_trophies = Paginator(trophies, 10)

        try:
            trophies = paginator_trophies.page(page)
        except PageNotAnInteger:
            trophies = paginator_trophies.page(1)
        except EmptyPage:
            trophies = paginator_trophies.page(paginator_trophies.num_pages)

        image_name = f"{team.slug}{team.id}.png"
        image_url = f"/media/images/teams/{image_name}"

        breadcrumbs = []

        if league_pk or country_pk:
            if country_pk:
                breadcrumbs += [
                    {'url': f"/countries/", 'name': "Países"},
                    {'url': f"/countries/country/{country.id}", 'name': country.name}
                ]
            if league_pk:
                if country_pk:
                    breadcrumbs += [
                        {'url': f"/countries/country/{country.id}/leagues/{league.id}", 'name': league.name}
                    ]
                else:
                    breadcrumbs += [
                        {'url': f"/leagues/", 'name': "Ligas"},
                        {'url': f"/leagues/league/{league.id}", 'name': league.name}
                    ]
            breadcrumbs += [
                {'url': "", 'name': team.name}
            ]
        else:
            breadcrumbs += [
                {'url': f"/teams/", 'name': 'Equipes'},
                {'url': "", 'name': team.name}
            ]

        context = {
            'team': team,
            'breadcrumbs': breadcrumbs,
            'players': players,
            'trophies': trophies,
            'stadium': stadium,
            'team_players_value': team_players_value,
            'related_country': related_country,
            'paginator_players': paginator_players,
            'paginator_trophies': paginator_trophies,
            'image_url': image_url,
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        team = get_object_or_404(Team, pk=pk)
        form = TeamColorForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect('team_detail', pk=pk)  # Redirect to the same team detail page after updating color
        # If form is not valid, re-render the team detail page with the form and team details
        context = {
            'team': team,
            'form': form,
            # Other context variables...
        }
        return render(request, self.template_name, context)
