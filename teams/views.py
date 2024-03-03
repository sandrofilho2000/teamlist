from .models import Team, TeamColorForm
from leagues.models import League
from league_team.models import LeaguesTeam  
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from players.models import Player

def order_list(list=[], key="", order=""):
    if key:
        list = list.order_by(f"{order}{key}")
    return list


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
        team = get_object_or_404(Team, pk=pk) 
        leagues_teams = LeaguesTeam.objects.filter(id_league=pk)
        leagues = [leagues_team.id_team for leagues_team in leagues_teams]
        form = TeamColorForm(instance=team)
        order_by_param = self.request.GET.get('field', 'id')
        order_dir_param = self.request.GET.get('order', 'asc')
        league_id = self.request.GET.get('league')
        
        if order_dir_param == "desc":
            order_dir_param = "-"
        else :
            order_dir_param = ""
        
        order = order_dir_param + order_by_param
        related_leagues = Team.objects.filter(pk__in=leagues)
        players = Player.objects.filter(id_team_id=pk).order_by(order)

                
        paginator = Paginator(players, 20) 
        page = request.GET.get('page')

        
        try:
            players = paginator.page(page)
        except PageNotAnInteger:
            players = paginator.page(1)
        except EmptyPage:
            players = paginator.page(paginator.num_pages)
            
            
        if league_id:
            league = League.objects.get(pk=league_id)
            breadcrumbs = [
                {'url': f"/leagues/", 'name': "Ligas"},
                {'url': f"/leagues/{league.id}/", 'name': league.name},
                {'url': f"/{team.id}/", 'name': team.name}
            ]
        else:
            breadcrumbs = [
                {'url': f"/teams/", 'name': "Equipes"},
                {'url': f"/{team.id}/", 'name': team.name}
            ]
        
        
        image_name = f"{team.slug}{team.id}.png"
        image_url = f"/static/images/teams/{image_name}"  
        

        context = {
            'team': team,
            'related_leagues': related_leagues,
            'players': players,
            'paginator': paginator,
            'breadcrumbs': breadcrumbs,
            'image_url': image_url,
            'form': form
        }
        
        
        return render(request, self.template_name, context )

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