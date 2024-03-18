from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, View
from countries.models import Country
from .models import League, LeagueColorForm
from teams.models import Team  
from league_team.models import LeaguesTeam  
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count

def order_list(list=[], key="", order=""):
    if key:
        list = list.order_by(f"{order}{key}")
    return list

class LeagueListView(ListView):
    model = League
    paginate_by = 50  

    def get_queryset(self):
        queryset = super().get_queryset()
        order_by_param = self.request.GET.get('field')
        order_dir_param = self.request.GET.get('order', 'asc') 
        queryset = queryset.annotate(num_teams=Count('leagues_teams'))

        
        if order_dir_param == 'desc':
            queryset = order_list(queryset, order_by_param, "-")
        else:
            queryset = order_list(queryset, order_by_param, "")

        return queryset

    
class LeagueInfoView(View):
    model = League

    template_name = 'leagues/league_detail.html'  

    def get(self, request, *args, **kwargs):
        
        pk = kwargs.get('pk')  
        country_pk = kwargs.get('country_pk')  
            
            
        league = get_object_or_404(League, pk=pk) 
        leagues_teams = LeaguesTeam.objects.filter(id_league=pk)
        teams = [leagues_team.id_team for leagues_team in leagues_teams]
        form = LeagueColorForm(instance=league)
        order_by_param = self.request.GET.get('field', 'id')
        order_dir_param = self.request.GET.get('order', 'asc')
        related_country = Country.objects.filter(pk=league.id_country_id).first()  
        
        if order_dir_param == "desc":
            order_dir_param = "-"
        else :
            order_dir_param = ""
        
        order = order_dir_param + order_by_param
        related_teams = Team.objects.filter(pk__in=teams).order_by(order) 
        related_teams_count = len(related_teams)
        paginator = Paginator(related_teams, 20) 
        page = request.GET.get('page')

        
        try:
            related_teams = paginator.page(page)
        except PageNotAnInteger:
            related_teams = paginator.page(1)
        except EmptyPage:
            related_teams = paginator.page(paginator.num_pages)
        
        breadcrumbs = []
        

        if country_pk:
            breadcrumbs+=[
                {'url': f"/countries/", 'name': "Países"},
                {'url': f"/countries/{country_pk}", 'name': related_country.name},
                {'url': f"", 'name': league.name}
            ]
        else:
            breadcrumbs += [
                {'url': f"/leagues/", 'name': "Ligas"},
                {'url': f"", 'name': league.name}
            ]
            
        

        
        
        
        image_name = f"{league.slug}{league.id}.webp"
        image_url = f"/media/images/leagues/{image_name}"  
        
        context = {
            'league': league,
            'related_teams': related_teams ,
            'main_item': league,
            'main_item_admin': f"/admin/league/{league.pk}/change/",
            'related_teams_count': related_teams_count,
            'paginator': paginator,
            'related_country': related_country,
            'breadcrumbs': breadcrumbs,
            'image_url': image_url,
            'form': form
        }
        
        if country_pk:
            context['country_pk'] = country_pk
        
        
        return render(request, self.template_name, context )

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        league = get_object_or_404(League, pk=pk)
        form = LeagueColorForm(request.POST, instance=league)
        
        if form.is_valid():
            form.save()
            return redirect('league_detail', pk=pk)
        
        # If form is not valid, re-render the league detail page with the form and league details
        context = {
            'league': league,
            'form': form,
            # Other context variables...
        }
        
        return render(request, self.template_name, context)