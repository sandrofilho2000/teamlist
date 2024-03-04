from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from countries.models import Country
from .models import CountryColorForm
from leagues.models import League
from teams.models import Team
from players.models import Player

def order_list(list=[], key="", order=""):
    if key:
        list = list.order_by(f"{order}{key}")
    return list



class CountryListView(ListView):
    model = Country
    paginate_by = 20  

    def get_queryset(self):
            queryset = super().get_queryset()
            queryset = queryset.annotate(num_teams=Count('team', distinct=True))
            queryset = queryset.annotate(num_leagues=Count('league', distinct=True))
            queryset = queryset.annotate(num_players=Count('player', distinct=True))
            order_by_param = self.request.GET.get('field')
            order_dir_param = self.request.GET.get('order', 'asc')  
            if order_dir_param == 'desc':
                queryset = order_list(queryset, order_by_param, "-")
            else:
                queryset = order_list(queryset, order_by_param, "")

            return queryset


class CountryDetailView(ListView):
    template_name = 'countries/country_detail.html'  

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')  
        
        order_by_param_league = self.request.GET.get('field', 'name')
        order_dir_param_league = self.request.GET.get('order', '')
        order_league = order_dir_param_league + order_by_param_league
        
        if order_dir_param_league == "desc":
            order_dir_param_league = "-"
        else :
            order_dir_param_league = ""

        
        order_by_param_team = self.request.GET.get('field', '-average_market_value')
        order_dir_param_team = self.request.GET.get('order', '')
        order_team = order_dir_param_team + order_by_param_team
        
        if order_dir_param_team == "desc":
            order_dir_param_team = "-"
        else :
            order_dir_param_team = ""
            
            
        order_by_param_player = self.request.GET.get('field', '-value_market')
        order_dir_param_player = self.request.GET.get('order', '')
        order_player = order_dir_param_player + order_by_param_player
        
        if order_dir_param_player == "desc":
            order_dir_param_player = "-"
        else :
            order_dir_param_player = ""


        country = get_object_or_404(Country, pk=pk) 
        leagues = League.objects.filter(id_country_id=pk).order_by(order_league)
        top_league = League.objects.filter(id_country_id=pk).order_by("balance").first()
        
        teams = Team.objects.filter(id_country_id=pk).order_by(order_team)
        top_team = Team.objects.filter(id_country_id=pk).order_by("-average_market_value").first()
        
        players = Player.objects.filter(id_country_id=pk).order_by(order_player)
        top_players = Player.objects.filter(id_team__id_country_id=pk).order_by("-value_market")[:3]

        
        form = CountryColorForm(instance=Country)
        

        

                
        image_name = f"{country.slug}{country.id}.png"
        country_flag = f"/media/images/countries/{image_name}"  
        
        page = request.GET.get('page')

        paginator = Paginator(leagues, 10) 
        paginator_teams = Paginator(teams, 10) 
        paginator_players = Paginator(players, 10) 

        
        try:
            leagues = paginator.page(page)
        except PageNotAnInteger:
            leagues = paginator.page(1)
        except EmptyPage:
            leagues = paginator.page(paginator.num_pages)
            
        
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
            
        context = {
            'country': country,
            'leagues': leagues,
            'top_league': top_league,
            'country_flag': country_flag,
            'players': players,
            'top_players': top_players,
            'teams': teams,
            'top_team': top_team,
            'paginator': paginator,
            'paginator_teams': paginator_teams,
            'paginator_players': paginator_players,
            'form': form
        }
                
        return render(request, self.template_name, context )


    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        country = get_object_or_404(Country, pk=pk)
        form = CountryColorForm(request.POST, instance=country)
        if form.is_valid():
            form.save()
            return redirect('country_detail', pk=pk)  # Redirect to the same country detail page after updating color
        # If form is not valid, re-render the country detail page with the form and country details
        context = {
            'country': country,
            'form': form,
            # Other context variables...
        }
        return render(request, self.template_name, context)



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



def map_view(request):
    model = Country.objects.all()
    context = {}
    context['countries'] = model
    return render(request, 'countries/country_list.html', context)


def country(request, iso_code):
    model = Country.objects.get(iso_a3=iso_code)
    context = {}
    context['country'] = model
    return render(request, 'countries/country_detail.html', context)