from otree.api import *

import random

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'complex'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    # Probability of HEADS:
    P_HEADS = .5

    # Tokens budget:
    TOKEN_BUDGET = 100


    # defining lotteries:
    # array for the first lottery:
    Lottery1 = [[0 for i in range(0,5)] for i in range(0,2)]
    Lottery1[0] = [90, 10]

    # array for the second lottery:
    Lottery2 = [[0 for i in range(0,5)] for i in range(0,2)]
    Lottery2[0] = [70, 30]

    # array for the third lottery:
    Lottery3 = [[0 for i in range(0,5)] for i in range(0,2)]
    Lottery3[0] = [50, 40]

    # array for the fourth lottery:
    Lottery4 = [[0 for i in range(0,5)] for i in range(0,2)]
    Lottery4[0] = [30, 60]

    # array for the fith lottery:
    Lottery5 = [[0 for i in range(0,5)] for i in range(0,2)]
    Lottery5[0] = [10, 90]

    # defining experts:
    EXPERTS_average_payoff = [0 for i in range(0,5)]
    EXPERTS_average_payoff = [2, 3, 4, 1, 6]

    EXPERTS_risk_rating = [0 for i in range(0,5)]
    EXPERTS_risk_rating = ['A', 'D', 'E', 'B', 'C']

    EXPERTS_quality_rating = [0 for i in range(0,5)]
    EXPERTS_quality_rating = ['D', 'A', 'B', 'C', 'E']

    EXPERTS_choices = [[[20 for i in range(0,5)] for i in range(0,5)] for i in range(0,5)]




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
    tokens = models.FloatField()

    delegation_choice = models.IntegerField()

    payment_round = models.IntegerField()

    # final investment
    final_choice_a1 = models.FloatField()
    final_choice_a2 = models.FloatField()
    final_choice_a3 = models.FloatField()
    final_choice_a4 = models.FloatField()
    final_choice_a5 = models.FloatField()

    # state of the world
    state_of_the_world = models.BooleanField(initial=False)


#-----------------------------------------------
# METHODS
#-----------------------------------------------
def set_payoffs(player: Player):
    player.payment_round = random.randint(1,C.NUM_ROUNDS)
    p = player.in_round(player.payment_round)
    choice = [0 for i in range(0,5)]
    if player.delegation_choice == -1:
        choice = [p.portfolio_shares_a1, p.portfolio_shares_a2, p.portfolio_shares_a3, p.portfolio_shares_a4, p.portfolio_shares_a5]
    else:
        choice = C.EXPERTS_choices[p.delegation_choice][player.payment_round-1]
    
    player.final_choice_a1 = choice[0]
    player.final_choice_a2 = choice[1]
    player.final_choice_a3 = choice[2]
    player.final_choice_a4 = choice[3]
    player.final_choice_a5 = choice[4]

    r = random.uniform(0,1)
    
    lottery_payoffs = [0 for i in range(0,5)]
    if r<C.P_HEADS:
        player.state_of_the_world = True
        lottery_payoffs = [C.Lottery1[player.payment_round-1][0], C.Lottery2[player.payment_round-1][0], C.Lottery3[player.payment_round-1][0], C.Lottery4[player.payment_round-1][0], C.Lottery5[player.payment_round-1][0]]
    else:
        player.state_of_the_world = False
        lottery_payoffs = [C.Lottery1[player.payment_round-1][1], C.Lottery2[player.payment_round-1][1], C.Lottery3[player.payment_round-1][1], C.Lottery4[player.payment_round-1][1], C.Lottery5[player.payment_round-1][1]]

    temp = 0
    for i in range(0,5):
        temp = temp+choice[i]*lottery_payoffs[i]/(C.TOKEN_BUDGET)

    player.payoff = temp




#--------------------------------------------
# PAGES
#--------------------------------------------
class Welcome(Page):
    pass

class DecisionScreen(Page):
    template_name = '_static/templates/Complex_DecisionScreen.html'
    form_model = 'player'
    form_fields = ['tokens', 'portfolio_shares_a1', 'portfolio_shares_a2', 'portfolio_shares_a3', 'portfolio_shares_a4', 'portfolio_shares_a5']

    @staticmethod
    def vars_for_template(player):
        i = player.subsession.round_number-1
        return dict(
            lottery_1 = C.Lottery1[i],
            lottery_2 = C.Lottery2[i],
            lottery_3 = C.Lottery3[i],
            lottery_4 = C.Lottery4[i],
            lottery_5 = C.Lottery5[i],
            )

    def error_message(player, values):
        if values['tokens']>0:
            return 'Please spend the entire budget'


class DelegationScreen(Page):
    def is_displayed(player):
        return player.subsession.round_number == C.NUM_ROUNDS

    template_name = '_static/templates/DelegationScreen.html'
    form_model = 'player'
    form_fields = ['delegation_choice']

    @staticmethod
    def vars_for_template(player):
        experts = [[0 for i in range(0,4)] for i in range(0,4)]
        for i in range(0,4):
            experts[i] = [C.EXPERTS_average_payoff[i], C.EXPERTS_risk_rating[i], C.EXPERTS_quality_rating[i], i]

        return dict(
            experts = [experts[i] for i in range(0,4)]
            )


class ResultsComputePage(Page):
    template_name = '_static/templates/ResultsComputePage.html'
    def is_displayed(player):
        return player.subsession.round_number == C.NUM_ROUNDS
    def before_next_page(player, timeout_happened):
        set_payoffs(player)

class Results(Page):
    def is_displayed(player):
        return player.subsession.round_number == C.NUM_ROUNDS

    @staticmethod
    def vars_for_template(player):
        i = player.payment_round-1
        return dict(
            lottery_1 = C.Lottery1[i],
            lottery_2 = C.Lottery2[i],
            lottery_3 = C.Lottery3[i],
            lottery_4 = C.Lottery4[i],
            lottery_5 = C.Lottery5[i],
            state_of_the_world = player.state_of_the_world
            )
#--------------------------------------------



#--------------------------------------------
# PAGE SEQUENCE
#--------------------------------------------
page_sequence = [
                Welcome,
                DecisionScreen,
                DelegationScreen,
                ResultsComputePage,
                Results
                ]
