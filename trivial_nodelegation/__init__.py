from otree.api import *

import random

doc = """
Your app description
"""

# models
class C(BaseConstants):
    NAME_IN_URL = 'trivial_nodelegation'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 2

    # Probability of HEADS:
    P_HEADS = .5

    # Number of experts to be used
    NUM_OF_EXPERTS = 2

    # defining lotteries:
    # array for the first lottery:
    Lottery1 = [[0 for i in range(0,5)] for i in range(0,2)]

    Lottery1[0] = [100, 0]
    Lottery1[1] = [0, 110]

    # array for the second lottery:
    Lottery2 = [[0 for i in range(0,5)] for i in range(0,2)]
    Lottery2[0] = [0, 100]
    Lottery2[1] = [110, 0]




class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # lottery choice:
    lottery_choice = models.IntegerField(min=1,max=2)

    # payment round
    payment_round = models.IntegerField(min=1,max=C.NUM_ROUNDS)

    # final choice:
    final_choice = models.IntegerField(initial=0)

    # state of the world
    state_of_the_world = models.BooleanField(initial=False)


#-----------------------------------------------
# METHODS
#-----------------------------------------------
def set_payoffs(player: Player):
    player.payment_round = random.randint(1,C.NUM_ROUNDS)
    p = player.in_round(player.payment_round)
    
    choice = p.lottery_choice
    

    player.final_choice = choice
    r = random.uniform(0,1)
    if choice == 1:
        if r<C.P_HEADS:
            player.state_of_the_world = True
            player.payoff = C.Lottery1[player.payment_round-1][0]
        else:
            player.state_of_the_world = False
            player.payoff = C.Lottery1[player.payment_round-1][1]
    if choice == 2:
        if r<C.P_HEADS:
            player.state_of_the_world = True
            player.payoff = C.Lottery2[player.payment_round-1][0]
        else:
            player.state_of_the_world = False
            player.payoff = C.Lottery2[player.payment_round-1][1]




#--------------------------------------------
# PAGES
#--------------------------------------------
class Welcome(Page):
    template_name = '_static/templates/Welcome.html'
    def is_displayed(player):
        return player.subsession.round_number == 1

class DecisionScreen(Page):
    template_name = '_static/templates/Trivial_DecisionScreen.html'
    form_model = 'player'
    form_fields = ['lottery_choice']

    @staticmethod
    def vars_for_template(player):
        i = player.subsession.round_number-1
        return dict(
            lottery_1 = C.Lottery1[i],
            lottery_2 = C.Lottery2[i],
            )

class ResultsComputePage(Page):
    template_name = '_static/templates/ResultsComputePage.html'
    def is_displayed(player):
        return player.subsession.round_number == C.NUM_ROUNDS
    def before_next_page(player, timeout_happened):
        set_payoffs(player)


class Results(Page):
#    template_name = '_static/templates/Trivial_Results.html'

    def is_displayed(player):
        return player.subsession.round_number == C.NUM_ROUNDS

    @staticmethod
    def vars_for_template(player):
        i = player.payment_round-1
        return dict(
            lottery_1 = C.Lottery1[i],
            lottery_2 = C.Lottery2[i],
            state_of_the_world = player.state_of_the_world
            )


page_sequence = [
                Welcome,
                DecisionScreen,
                ResultsComputePage, 
                Results
                ]


