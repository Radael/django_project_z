from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='index'),
    path('teams/<slug:teams_slug>/', TeamDetailView.as_view(), name='teams'),
    path('players/<slug:players_slug>/', PlayerDetailView.as_view(), name='players'),
    path('tournaments/<slug:tournaments_slug>/', TournamentDetailView.as_view(), name='tournaments'),
    path('teams/', TeamPage.as_view(), name='teams'),
    path('players/', PlayerPage.as_view(), name='players'),
    path('add-tournament/', AddDotaTournament.as_view(), name='add_tournament'),
    path('update-tournament/<slug:tournaments_slug>/', UpdateDotaTournament.as_view(), name='update_tournament'),
    path('delete-tournament/<slug:tournaments_slug>/', DeleteDotaTournament.as_view(), name='delete_tournament'),
    path('team/add-team/', AddDotaTeam.as_view(), name='add_team'),
    path('team/update-team/<slug:teams_slug>', UpdateDotaTeam.as_view(), name='update_team'),
    path('delete-team/<slug:teams_slug>/', DeleteDotaTeam.as_view(), name='delete_team'),
    path('player/add-player/', AddDotaPlayer.as_view(), name='add_player'),
    path('player/update-player/<slug:players_slug>', UpdateDotaPlayer.as_view(), name='update_player'),
    path('delete-player/<slug:players_slug>/', DeleteDotaPlayer.as_view(), name='delete_player'),
]
