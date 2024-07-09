from django.db import models

from teams.models import Team
from trophies.models import Trophy

class TeamTrophy(models.Model):
    id_team = models.ForeignKey(Team, related_name='team_trophy', on_delete=models.CASCADE)
    id_trophy = models.ForeignKey(Trophy, related_name='team_trophy', on_delete=models.CASCADE)
    season = models.CharField(
        verbose_name="Temporada", max_length=255, null=False, blank=False
    )
    
    def last_champion_info(self):
        last_champion = TeamTrophy.objects.filter(
            id_trophy=self.id_trophy
        ).order_by('-season').first()
        if last_champion:
            return last_champion.id_team
        return None

    class Meta:
        db_table = 'team_trophy'  
        verbose_name_plural = "Equipes e troféus"
        verbose_name = 'Equipe e troféu'
