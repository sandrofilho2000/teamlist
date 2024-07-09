from django.urls import path
from . import views

urlpatterns = [
    path("api/design_ui", views.getDesignUi),
    path("api/country-counts", views.country_counts),
]
