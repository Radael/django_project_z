from django.db import models
from django_countries.fields import CountryField
from django.urls import reverse


class DotaTeam(models.Model):
    team_name = models.CharField(max_length=50, verbose_name='Team Name')
    slug = models.SlugField(max_length=255, db_index=True, verbose_name='url')
    team_logo = models.ImageField(verbose_name='Team Logo', upload_to='teams')
    short_name = models.CharField(max_length=10, verbose_name='Short Name')
    team_location = CountryField(verbose_name='Country')
    total_earning = models.IntegerField(verbose_name='Earnings')

    class Meta:
        verbose_name = 'Dota Team'
        verbose_name_plural = 'Dota Teams'
        ordering = ['id']

    def __str__(self):
        return self.short_name

    def get_players(self):
        return self.players.all()

    def get_absolute_url(self):
        # slug = ('-'.join(self.team_name.split())).lower()
        return reverse('teams', kwargs={'teams_slug': self.slug})


class DotaPlayer(models.Model):
    ROLE_CHOICES = [
        (1, 'Carry'),
        (2, 'Mid'),
        (3, 'Offlane'),
        (4, 'SoftSupport'),
        (5, 'HardSupport'),
        (6, 'Jungle'),
        (7, 'Coach')
    ]

    nickname = models.CharField(verbose_name='Nickname', max_length=50, unique=True)
    slug = models.SlugField(max_length=255, db_index=True, verbose_name='url')
    player_photo = models.ImageField(verbose_name='Player photo', blank=True, upload_to='players')
    name = models.CharField(verbose_name='Name', max_length=250, null=True)
    surname = models.CharField(verbose_name='Surname', max_length=250, null=True)
    nationality = CountryField(verbose_name='Country', null=True)
    born = models.DateField(verbose_name='Date of birth', null=True)
    role = models.IntegerField(verbose_name='Role', choices=ROLE_CHOICES, default='1')
    mmr = models.IntegerField(verbose_name='ММР', default=0)
    team = models.ForeignKey(DotaTeam, on_delete=models.PROTECT, null=True, blank=True, related_name='players')

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'
        ordering = ['nickname']

    def __str__(self):
        return f'{self.team} {self.nickname}'

    def get_absolute_url(self):
        return reverse('players', kwargs={'players_slug': self.slug})


class DotaTournament(models.Model):
    TIER_CHOICES = [
        (1, 'International'),
        (2, 'Major'),
        (3, 'DPC'),
        (4, 'Other'),
    ]

    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, db_index=True, verbose_name='url')
    photo = models.ImageField(verbose_name='Tournament photo', blank=True, upload_to='tournaments')
    tier = models.IntegerField(choices=TIER_CHOICES, default=4, verbose_name='tournament tier')
    teams = models.ManyToManyField(DotaTeam, verbose_name='Teams')
    prize_pool = models.IntegerField(default=0, null=True, verbose_name='Prize pool')
    patch = models.CharField(max_length=5, default='6.76', verbose_name='Patch')
    event_date = models.DateField(verbose_name='Date', null=True)
    end_event_date = models.DateField(null=True)
    location = CountryField(null=True, verbose_name='Country')

    class Meta:
        verbose_name = 'Tournament'
        verbose_name_plural = 'Tournaments'
        ordering = ['event_date']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tournaments', kwargs={'tournaments_slug': self.slug})

    def get_teams(self):
        return self.teams.all()
