import re
from team_trophy.models import TeamTrophy
from trophies.models import Trophy
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, View
from teams.models import Team  
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count


def order_list(list=[], key="", order=""):
    if key:
        list = list.order_by(f"{order}{key}")
    return list



class TeamTrophyListView(ListView):
    model = TeamTrophy
    paginate_by = 50  
    template_name = 'team_trophy/team_trophy_list.html' 
    
    def get_queryset(self):
        queryset = super().get_queryset()

        queryset = queryset.values('id_trophy', 'id_trophy__name', 'id_trophy__img').annotate(editions_count=Count('id_trophy'))

        order_by_param = self.request.GET.get('field', 'id_trophy__name')
        order_dir_param = self.request.GET.get('order', 'desc')  
        if order_dir_param == 'desc':
            queryset = sorted(queryset, key=lambda x: x[order_by_param], reverse=True)
        else:
            queryset = sorted(queryset, key=lambda x: x[order_by_param])

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    
    
 
class TeamTrophyInfoView(View):
    model = TeamTrophy

    template_name = 'team_trophy/team_trophy_detail.html'  

    def get(self, request, *args, **kwargs):
        
        pk = kwargs.get('pk')  
        order_by_param = self.request.GET.get('field', 'season')
        order_dir_param = self.request.GET.get('order', 'desc')
        
        if order_dir_param == "desc":
            order_dir_param = "-"
        else :
            order_dir_param = ""
        
        order = order_dir_param + order_by_param
            
        trophy = get_object_or_404(Trophy, pk=pk) 
        related_teams = TeamTrophy.objects.filter(id_trophy=pk).order_by(order)
        greatest_champion_id = related_teams.values('id_team').annotate(count=Count('id_team')).order_by('-count').first()
        greatest_champion = get_object_or_404(Team, pk=greatest_champion_id['id_team'])
        editions_count = len(related_teams)
        paginator = Paginator(related_teams, 20) 
        page = request.GET.get('page')

        
        try:
            related_teams = paginator.page(page)
        except PageNotAnInteger:
            related_teams = paginator.page(1)
        except EmptyPage:
            related_teams = paginator.page(paginator.num_pages)
        
 
        context = {
            'trophy': trophy,
            'paginator': paginator,
            'greatest_champion': greatest_champion,
            'related_teams': related_teams,
            'editions_count': editions_count
        }
        

        
        
        return render(request, self.template_name, context )

    