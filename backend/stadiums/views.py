from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render
from django.views import View
from teams.models import Team
from stadiums.models import Stadium

# Utility function for ordering lists
def order_list(list=[], key="", order=""):
    if key:
        list = list.order_by(f"{order}{key}")
    return list

# View for listing stadiums
class StadiumListView(ListView):
    model = Stadium
    paginate_by = 20  

    def get_queryset(self):
        queryset = super().get_queryset()

        # Get ordering parameters from request, default to 'build_value' descending
        order_by_param = self.request.GET.get('field', 'build_value')
        order_dir_param = self.request.GET.get('order', 'desc')  

        # Order queryset based on parameters
        if order_dir_param == 'desc':
            queryset = order_list(queryset, order_by_param, "-")
        else:
            queryset = order_list(queryset, order_by_param, "")

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

# View for displaying stadium details
class StadiumInfoView(View):
    model = Stadium
    template_name = 'stadiums/stadium_detail.html'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        team_pk = kwargs.get('team_pk')
        team = Team.objects.filter(pk=team_pk).first()

        # Retrieve stadium object or raise 404 if not found
        stadium = get_object_or_404(Stadium, pk=pk)
        
        # Split stadium images string into a list
        imgs = stadium.imgs.split("%%") if stadium.imgs else []

        # Filter out empty strings from the list
        imgs = [img for img in imgs if img]
        
        # If no images found, use a default placeholder image
        if not imgs:
            imgs = ["https://t4.ftcdn.net/jpg/04/17/36/11/360_F_417361125_RnrhT3Np0zB0UpeD7QlwuOoyghEGGjBX.jpg"]
            
        breadcrumbs = []

        # Build breadcrumbs based on whether a team is associated with the stadium
        if team_pk:
            breadcrumbs += [
                {'url': f"/teams/", 'name': "Equipes"},
                {'url': f"/teams/{team_pk}", 'name': team.name},
                {'url': f"#", 'name': stadium.name}
            ]
        else:
            breadcrumbs += [
                {'url': f"/stadiums/", 'name': 'Estádios'},
                {'url': "", 'name': stadium.name}
            ]
        
        context = {
            'breadcrumbs':breadcrumbs,
            'stadium': stadium,
            'imgs': imgs
        }

        return render(request, self.template_name, context)
