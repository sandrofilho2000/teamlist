from teams.models import Team

def team_list_processor(request):
    team_list = Team.objects.all()  # Assuming Team is the model representing your teams
    return {'team_list': team_list}
