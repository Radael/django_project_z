from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, DeleteView, CreateView, UpdateView
from django.views import View
from django.db.models import Q

from .models import *
from .utils import *
from .forms import *


class HomePage(ContextMixin, ListView):
    model = DotaTournament
    template_name = 'main/index.html'
    context_object_name = 'tourns'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            self.get_user_context(title="Главная страница"),
            form=DotaTournamentTierSearch,
            add='add_tournament',
        )
        return context

    def get_ordering(self):
        ordering = super().get_ordering()
        if ordering:
            return ordering
        return ['event_date']

    def get_queryset(self):
        qs = DotaTournament.objects.all()

        tier = self.request.GET.get('dotatournament_tier')
        if tier and tier != '0':
            qs = qs.filter(Q(tier=int(tier)))
        ordering = self.get_ordering()
        qs = qs.order_by(*ordering)
        return qs


class TeamPage(ContextMixin, ListView):
    model = DotaTeam
    template_name = 'main/teams.html'
    context_object_name = 'teams'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(title="Команды"), add='add_team')
        return context


class PlayerPage(ContextMixin, ListView):
    model = DotaPlayer
    template_name = 'main/players.html'
    context_object_name = 'players'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(title="Игроки"), add='add_player')
        return context


class TeamDetailView(ContextMixin, DetailView):
    model = DotaTeam
    template_name = 'main/team.html'
    slug_url_kwarg = 'teams_slug'
    context_object_name = 'teams'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context = self.get_user_context(**context)
        return context


class PlayerDetailView(ContextMixin, DetailView):
    model = DotaPlayer
    template_name = 'main/player.html'
    slug_url_kwarg = 'players_slug'
    context_object_name = 'players'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context = self.get_user_context(**context)
        return context


class TournamentDetailView(ContextMixin, DetailView):
    model = DotaTournament
    template_name = 'main/tournament.html'
    slug_url_kwarg = 'tournaments_slug'
    context_object_name = 'tournaments'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context = self.get_user_context(**context)
        return context


class AddDotaTeam(ContextMixin, CreateView):
    model = DotaTeam
    template_name = 'main/team_form.html'
    form_class = AddTeamForm
    success_url = reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(title="Добавить команду"))
        return context


class AddDotaPlayer(ContextMixin, CreateView):
    model = DotaPlayer
    template_name = 'main/player_form.html'
    form_class = AddPlayerForm
    success_url = reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(title="Добавить игрока"))
        return context


class AddDotaTournament(ContextMixin, CreateView):
    model = DotaTournament
    form_class = AddTournamentForm
    template_name = 'main/tournament_form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(title="Добавить турнир"))
        return context


class UpdateDotaTeam(ContextMixin, UpdateView):
    model = DotaTeam
    template_name = 'main/team_form.html'
    form_class = AddTeamForm
    slug_url_kwarg = 'teams_slug'
    success_url = reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        team_name = self.object.team_name if self.object else ''
        context.update(self.get_user_context(title=f'Изменить {team_name}'))
        return context


class UpdateDotaPlayer(ContextMixin, UpdateView):
    model = DotaPlayer
    template_name = 'main/player_form.html'
    form_class = AddPlayerForm
    slug_url_kwarg = 'players_slug'
    success_url = reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        player_name = self.object.nickname if self.object else ''
        context.update(self.get_user_context(title=f'Изменить {player_name}'))
        return context


class UpdateDotaTournament(ContextMixin, UpdateView):
    model = DotaTournament
    template_name = 'main/tournament_form.html'
    form_class = AddTournamentForm
    slug_url_kwarg = 'tournaments_slug'
    success_url = reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        tournament_name = self.object.name if self.object else ''
        context.update(self.get_user_context(title=f'Изменить {tournament_name}'))
        return context


class DeleteDotaTournament(ContextMixin, DeleteView):
    model = DotaTournament
    template_name = 'main/delete_tournament.html'
    slug_url_kwarg = 'tournaments_slug'
    success_url = reverse_lazy('index')


class DeleteDotaTeam(ContextMixin, DeleteView):
    model = DotaTeam
    template_name = 'main/delete_team.html'
    slug_url_kwarg = 'teams_slug'
    success_url = reverse_lazy('teams')


class DeleteDotaPlayer(ContextMixin, DeleteView):
    model = DotaPlayer
    template_name = 'main/delete_player.html'
    slug_url_kwarg = 'players_slug'
    success_url = reverse_lazy('players')
