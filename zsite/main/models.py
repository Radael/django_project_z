from django.db import models
from django_countries.fields import CountryField


class DotaTeam(models.Model):
    team_name = models.CharField('Name', max_length=50)
    # team_location = models.CharField('Country', max_length=250)
    team_location = CountryField()
    total_earning = models.IntegerField('Earnings ($)')

    def __str__(self):
        return self.team_name

    class Meta:
        verbose_name = 'Dota Team'
        verbose_name_plural = 'Dota Teams'


class DotaPlayer(models.Model):

    ROLE_CHOICES = [
        ('1', 'Carry'),
        ('2', 'Mid'),
        ('3', 'Offlane'),
        ('4', 'SoftSupport'),
        ('5', 'HardSupport'),
        ('6', 'Jungle'),
        ('7', 'Coach')
    ]

    nickname = models.CharField('Nickname', max_length=50, unique=True)
    name = models.CharField('Name', max_length=250)
    surname = models.CharField('Surname', max_length=250)
    # nationality = models.CharField('Country', max_length=250)
    nationality = CountryField()
    born = models.DateField('Date of birth')
    role = models.CharField(max_length=1, choices=ROLE_CHOICES, default='1')
    mmr = models.IntegerField('ММР', default=0)
    team = models.ForeignKey(DotaTeam, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.team} {self.nickname}'

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'


class DotaTournamentHandler(models.Model):
    name = models.CharField(max_length=255, unique=True)
    teams = models.ManyToManyField(DotaTeam)
    prize_pool = models.IntegerField('Prize pool', default=0, null=True)
    patch = models.CharField('Patch', max_length=5, default='6.76')
    event_date = models.DateField('Date')
    location = CountryField()

    def __str__(self):
        return self.name


class DotaPlayerQuotes(models.Model):
    players = models.ManyToManyField(DotaPlayer)
    quote = models.SlugField(max_length=255, unique=True, null=True)

    def __str__(self):
        nationality_list = [player.nationality for player in self.players.all()]
        if 'UA' in nationality_list:
            return 'Хрю-Хрю'
        else:
            return ', '.join([player.name for player in self.players.all()])
