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
    path("leagues/<int:pk>/", LeagueInfoView.as_view(), name="league_detail"),  
    path("leagues/<int:pk>/", LeagueInfoView.as_view(), name="league_detail"),  
    path("leagues/", LeagueListView.as_view(), name="league_list"),
    path("", CountryListView.as_view(), name='country_list'),
    path("country/<int:pk>", CountryDetailView.as_view(), name='country_detail'),
    path("teams/", TeamListView.as_view(), name="team_list"),
    path("teams/<int:pk>/", TeamInfoView.as_view(), name="team_detail"), 
    path("", include("api.urls")),  # Include API URLs
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += path("__debug__/", include("debug_toolbar.urls")),