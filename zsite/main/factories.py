import factory
from faker import Factory

from .models import DotaTeam

factory_en = Factory.create('en-EN')


class TeamFactory(factory.django.DjangoModelFactory):
    team_name = factory.Faker('team_name')
    slug = factory.Faker('slug')
    team_logo = factory.Faker('team_logo')
    short_name = factory.Faker('short_name')
    team_location = factory.Faker('team_location')
    total_earning = factory.Faker('total_earning')

    class Meta:
        model = DotaTeam
