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
    """
    Function to order queryset based on given key and order parameters.
    """
    if key:
        return queryset.order_by(f"{order}{key}")
    return queryset


class TeamListView(ListView):
    """
    ListView to display a list of teams.
    """

    model = Team
    paginate_by = 50

    def get_queryset(self):
        """
        Get queryset of teams and handle ordering based on request parameters.
        """
        queryset = super().get_queryset()
        order_by_param = self.request.GET.get("field")
        order_dir_param = self.request.GET.get("order", "asc")
        queryset = queryset.annotate(num_leagues=Count("leagues_teams"))

        if order_dir_param == "desc":
            queryset = order_list(queryset, order_by_param, "-")
        else:
            queryset = order_list(queryset, order_by_param, "")

        return queryset


class TeamInfoView(View):
    """
    View to display team information.
    """

    model = League
    template_name = "teams/team_detail.html"

    def get(self, request, *args, **kwargs):
        """
        Handle GET request to display team details.
        """
        pk = kwargs.get("pk")
        league_pk = kwargs.get("league_pk")
        country_pk = kwargs.get("country_pk")

        if league_pk:
            league = get_object_or_404(League, pk=league_pk)

        team = get_object_or_404(Team, pk=pk)
        country = Country.objects.filter(pk=team.id_country_id).first()
        stadium = Stadium.objects.filter(pk=team.id_stadium_id).first()
        form = TeamColorForm(instance=team)
        related_country = Country.objects.filter(pk=team.id_country_id).first()
        page = request.GET.get("page")

        # Handle player ordering
        order_dir_param_player = self.request.GET.get("order_player", "")
        if order_dir_param_player == "desc":
            order_player = "-"
        else:
            order_player = ""
        order_by_param_player = self.request.GET.get("field_player", "-value_market")
        order_player += order_by_param_player
        players = Player.objects.filter(id_team_id=pk).order_by(order_player)
        team_players_value = players.aggregate(total_value=Sum("value_market"))[
            "total_value"
        ]
        paginator_players = Paginator(players, 10)

        # Handle trophy ordering
        order_by_param_trophy = self.request.GET.get("field_trophy", "season")
        if order_by_param_trophy:
            if order_by_param_trophy == "name":
                order_by_param_trophy = f"id_trophy__{order_by_param_trophy}"
        order_dir_param_trophy = self.request.GET.get("order_trophy", "asc")
        if order_dir_param_trophy == "desc":
            order_trophy = "-"
        else:
            order_trophy = ""
        order_trophy += order_by_param_trophy
        trophies = team.team_trophy.all().order_by(order_trophy)
        paginator_trophies = Paginator(trophies, 10)

        breadcrumbs = []

        # Prepare breadcrumbs based on league and country
        if league_pk or country_pk:
            if country_pk:
                breadcrumbs += [
                    {"url": f"/countries/", "name": "Países"},
                    {"url": f"/countries/{country.id}", "name": country.name},
                ]
            if league_pk:
                if country_pk:
                    breadcrumbs += [
                        {
                            "url": f"/countries/{country.id}/leagues/{league.id}",
                            "name": league.name,
                        }
                    ]
                else:
                    breadcrumbs += [
                        {"url": f"/leagues/", "name": "Ligas"},
                        {"url": f"/league/{league.id}", "name": league.name},
                    ]
            breadcrumbs += [{"url": "", "name": team.name}]
        else:
            breadcrumbs += [
                {"url": f"/teams/", "name": "Equipes"},
                {"url": "", "name": team.name},
            ]

        context = {
            "team": team,
            "main_item": team if request.user.has_perm("teams.change_team") else False,
            "main_item_admin": (
                f"/admin/teams/team/{team.pk}/change/"
                if request.user.has_perm("teams.change_team")
                else False
            ),
            "team_img": team.img.replace("/medium/", "/big/"),
            "breadcrumbs": breadcrumbs,
            "players": players,
            "trophies": trophies,
            "stadium": stadium,
            "team_players_value": team_players_value,
            "related_country": related_country,
            "paginator_players": paginator_players,
            "paginator_trophies": paginator_trophies,
            "form": form,
            "country_pk": country_pk,
            "league_pk": league_pk,
        }

        print(team)

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """
        Handle POST request to update team color preferences.
        """
        pk = kwargs.get("pk")
        team = get_object_or_404(Team, pk=pk)
        form = TeamColorForm(request.POST, instance=team)

        if form.is_valid():
            if request.user.has_perm("teams.change_team"):
                form.save()

            return redirect("team_detail", pk=pk)

        context = {
            "team": team,
            "form": form,
        }

        return render(request, self.template_name, context)


def handler404(request, exception):
    """
    Custom 404 error handler.
    """
    # Render the 404.html template
    return render(request, "templates/atomic/pages/404.html", status=404)
