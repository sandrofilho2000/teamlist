from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView
from django.db.models import Count

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
        order_by_param = self.request.GET.get('field', 'name')
        order_dir_param = self.request.GET.get('order', '')
        order = order_dir_param + order_by_param

        country = get_object_or_404(Country, pk=pk) 
        players = Player.objects.filter(id_country_id=pk).order_by(order)
        leagues = League.objects.filter(id_country_id=pk).order_by(order)
        form = CountryColorForm(instance=Country)
        
        if order_dir_param == "desc":
            order_dir_param = "-"
        else :
            order_dir_param = ""
        
        order = order_dir_param + order_by_param

                
        image_name = f"{country.slug}{country.id}.png"
        country_flag = f"/media/images/countries/{image_name}"  
            

        context = {
            'country': country,
            'leagues': leagues,
            'country_flag': country_flag,
            'players': players,
            'form': form
        }
        
        print("country_flag: ", country_flag)
        
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