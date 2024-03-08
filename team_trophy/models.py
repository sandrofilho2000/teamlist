from django.db import models

from teams.models import Team
from trophies.models import Trophy

# Create your models here.
class TeamTrophy(models.Model):
    id_team = models.ForeignKey(Team, related_name='team_trophy', on_delete=models.CASCADE)
    id_trophy = models.ForeignKey(Trophy, related_name='team_trophy', on_delete=models.CASCADE)
    season = models.CharField(
        verbose_name="Temporada", max_length=255, null=False, blank=False
    )

    class Meta:
        db_table = 'team_trophy'  # Specify the database table name
