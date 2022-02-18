from otree.api import *

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'complex'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    # Probability of HEADS:
    P_HEADS = .5


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # defining the shares for the different assets:
    portfolio_shares_a1 = models.FloatField()
    portfolio_shares_a2 = models.FloatField()
    portfolio_shares_a3 = models.FloatField()
    portfolio_shares_a4 = models.FloatField()
    portfolio_shares_a5 = models.FloatField()

#--------------------------------------------
# PAGES
#--------------------------------------------
class DecisionScreen(Page):
    form_model = 'player'
    form_fields = ['portfolio_shares_a1', 'portfolio_shares_a2', 'portfolio_shares_a3', 'portfolio_shares_a4', 'portfolio_shares_a5']

#--------------------------------------------



#--------------------------------------------
# PAGE SEQUENCE
#--------------------------------------------
page_sequence = [DecisionScreen]
