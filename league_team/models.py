from django.db import models
from leagues.models import League  # Import the League model
from teams.models import Team  # Import the Team model

class LeaguesTeam(models.Model):
    id_league = models.ForeignKey(League, related_name='leagues_teams', on_delete=models.CASCADE)
    id_team = models.ForeignKey(Team, related_name='leagues_teams', on_delete=models.CASCADE)

    class Meta:
        db_table = 'leagues_teams'  # Specify the database table name
