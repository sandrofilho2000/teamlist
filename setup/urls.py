from django.conf import settings
from countries.views import CountryListView, CountryDetailView
from leagues.views import LeagueListView, LeagueInfoView
from search_items.views import SearchItemsView
from teams.views import TeamListView, TeamInfoView
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("search_items/<str:query>/", SearchItemsView.as_view(), name="search_items"),  
    path("", include("api.urls")),  # Include API URLs
    path("", TeamListView.as_view(), name="team_list"),
]

countries_patterns = [
    path("countries/country/<int:pk>", CountryDetailView.as_view(), name='countries_detail'),
    path("country/<int:pk>", CountryDetailView.as_view(), name='country_detail'),
    path("countries/", CountryListView.as_view(), name='country_list'),
]

leagues_patterns = [
    path("countries/country/<int:country_pk>/leagues/<int:pk>/", LeagueInfoView.as_view(), name="country_league_detail"),  
    path("leagues/league/<int:pk>/", LeagueInfoView.as_view(), name="league_detail"),  
    path("leagues/", LeagueListView.as_view(), name="league_list"),
]

teams_patterns = [
    path("countries/country/<int:country_pk>/teams/<int:pk>/", TeamInfoView.as_view(), name="country_team_detail"), 
    path("countries/country/<int:country_pk>/leagues/<int:league_pk>/teams/<int:pk>/", TeamInfoView.as_view(), name="country_league_team_detail"), 
    path("leagues/<int:league_pk>/teams/<int:pk>/", TeamInfoView.as_view(), name="league_team_detail"), 
    path("teams/<int:pk>/", TeamInfoView.as_view(), name="team_detail"), 
    path("teams/", TeamListView.as_view(), name="team_list"),
]

urlpatterns += countries_patterns
urlpatterns += leagues_patterns
urlpatterns += teams_patterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += path("__debug__/", include("debug_toolbar.urls")),