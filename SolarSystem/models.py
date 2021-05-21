from django.db import models


class Question(models.Model):
    variant_1 = models.CharField(max_length=500)
    variant_2 = models.CharField(max_length=500)
    votes_for_1 = models.IntegerField()
    votes_for_2 = models.IntegerField()

    def total_votes(self):
        return self.votes_for_1 + self.votes_for_2

    def percent_1(self):
        return int(self.votes_for_1 / self.total_votes() * 10000) / 100.0

    def percent_2(self):
        return int(self.votes_for_2 / self.total_votes() * 10000) / 100.0

    def __str__(self):
        return str(self.pk)


class Propose(models.Model):
    variant_1 = models.CharField(max_length=500)
    variant_2 = models.CharField(max_length=500)
