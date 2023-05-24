from django.test import TestCase
from django.urls import reverse

from .models import DotaTeam


class TestDotaTeam(TestCase):

    # def setUp(self):
    #     self.team = DotaTeam.objects.create(
    #         team_name='Team Test',
    #         slug='team-test',
    #         short_name='Test',
    #         team_location='UA',
    #         total_earning=10000
    #     )

    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_teams(self):
        response = self.client.get(reverse('players'))
        self.assertEqual(response.status_code, 200)

    def test_players(self):
        response = self.client.get(reverse('players'))
        self.assertEqual(response.status_code, 200)

    def test_tournaments(self):
        response = self.client.get(reverse('add_tournament'))
        self.assertEqual(response.status_code, 200)
