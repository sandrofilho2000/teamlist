from django.conf import settings
from countries.views import CountryListView, CountryDetailView
from leagues.views import LeagueListView, LeagueInfoView
from players.views import PlayerInfoView, PlayerListView
from search_items.views import SearchItemsView
from stadiums.views import StadiumInfoView, StadiumListView
from team_trophy.views import TeamTrophyInfoView, TeamTrophyListView
from teams.views import TeamListView, TeamInfoView
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from trophies.views import TrophyListView


urlpatterns = [
    path("search_items/<str:query>/", SearchItemsView.as_view(), name="search_items"),  
    path("", TeamListView.as_view(), name="team_list"),
    path("admin/", admin.site.urls),
    path("", include("api.urls")),  
]

countries_patterns = [
    path("countries/<int:pk>", CountryDetailView.as_view(), name='countries_detail'),
    path("country/<int:pk>", CountryDetailView.as_view(), name='country_detail'),
    path("countries/", CountryListView.as_view(), name='country_list'),
]

leagues_patterns = [
    path("countries/<int:country_pk>/leagues/<int:pk>/", LeagueInfoView.as_view(), name="country_league_detail"),  
    path("league/<int:pk>/", LeagueInfoView.as_view(), name="league_detail"),  
    path("leagues/", LeagueListView.as_view(), name="league_list"),
]

players_patterns = [
    path("countries/<int:country_pk>/leagues/<int:league_pk>/teams/<int:team_pk>/player/<int:pk>", PlayerInfoView.as_view(), name="country_league_team_player_detail"),
    path("countries/<int:country_pk>/teams/<int:team_pk>/player/<int:pk>", PlayerInfoView.as_view(), name="country_team_player_detail"),
    path("leagues/<int:league_pk>/teams/<int:team_pk>/player/<int:pk>", PlayerInfoView.as_view(), name="league_team_player_detail"),
    path("countries/<int:country_pk>/player/<int:pk>", PlayerInfoView.as_view(), name="country_player_detail"),
    path("teams/<int:team_pk>/player/<int:pk>", PlayerInfoView.as_view(), name="team_player_detail"),
    path("players/player/<int:pk>", PlayerInfoView.as_view(), name="player_detail"),
    path("players/", PlayerListView.as_view(), name="player_list"),
]

trophies_patterns = [
    path("countries/<int:country_pk>/leagues/<int:league_pk>/teams/<int:team_pk>/trophy/<int:pk>", TeamTrophyInfoView.as_view(), name="country_league_team_trophy_detail"),
    path("countries/<int:country_pk>/teams/<int:team_pk>/trophy/<int:pk>", TeamTrophyInfoView.as_view(), name="country_team_trophy_detail"),
    path("leagues/<int:league_pk>/teams/<int:team_pk>/trophy/<int:pk>", TeamTrophyInfoView.as_view(), name="league_team_trophy_detail"),
    path("teams/<int:team_pk>/trophy/<int:pk>", TeamTrophyInfoView.as_view(), name="team_trophy_detail"),
    path("trophies/trophy/<int:pk>", TeamTrophyInfoView.as_view(), name="trophy_detail"),
    path("trophies/", TeamTrophyListView.as_view(), name="trophy_list"),
]

teams_patterns = [
    path("countries/<int:country_pk>/leagues/<int:league_pk>/teams/<int:pk>/", TeamInfoView.as_view(), name="country_league_team_detail"), 
    path("countries/<int:country_pk>/teams/<int:pk>/", TeamInfoView.as_view(), name="country_team_detail"), 
    path("leagues/<int:league_pk>/teams/<int:pk>/", TeamInfoView.as_view(), name="league_team_detail"), 
    path("teams/<int:pk>/", TeamInfoView.as_view(), name="team_detail"), 
    path("teams/", TeamListView.as_view(), name="team_list"),
]

stadiums_patterns = [
    path("stadium/<int:pk>/", StadiumInfoView.as_view(), name="stadium_detail"), 
    path("stadiums/", StadiumListView.as_view(), name="stadium_list"),
]

urlpatterns += countries_patterns
urlpatterns += leagues_patterns
urlpatterns += teams_patterns
urlpatterns += stadiums_patterns
urlpatterns += players_patterns
urlpatterns += trophies_patterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += path("__reload__/", include("django_browser_reload.urls")),
urlpatterns += path('i18n/', include('django.conf.urls.i18n')), 

handler404 = 'teams.views.handler404'


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += path("__debug__/", include("debug_toolbar.urls")),