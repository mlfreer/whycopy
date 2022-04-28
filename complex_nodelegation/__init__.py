from otree.api import *

import random

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'complex_nodelegation'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 5

    # Probability of HEADS:
    P_HEADS = .5

    # Tokens budget:
    EXCHANGE_RATE = 1000
    TOKEN_BUDGET = 100

    Lottery1 = [[0 for i in range(0,5)] for i in range(0,5)]
    Lottery2 = [[0 for i in range(0,5)] for i in range(0,5)]
    Lottery3 = [[0 for i in range(0,5)] for i in range(0,5)]
    Lottery4 = [[0 for i in range(0,5)] for i in range(0,5)]
    Lottery5 = [[0 for i in range(0,5)] for i in range(0,5)]
    Lottery6 = [[0 for i in range(0,5)] for i in range(0,5)]

    # defining lotteries:
    # array for the first lottery:
    
    
    Lottery1[0] = [55, 15]
    Lottery1[1] = [40, 20]
    Lottery1[2] = [10, 70]
    Lottery1[3] = [100, 0]
    Lottery1[4] = [18, 10]

    # array for the second lottery:
    Lottery2[0] = [68, 16]
    Lottery2[1] = [13, 27]
    Lottery2[2] = [10, 50]
    Lottery2[3] = [50, 10]
    Lottery2[4] = [16, 20]

    # array for the third lottery:
    Lottery3[0] = [40, 30]
    Lottery3[1] = [91, 3]
    Lottery3[2] = [20, 40]
    Lottery3[3] = [20, 16]
    Lottery3[4] = [0, 100]

    # array for the fourth lottery:
    
    Lottery4[0] = [88, 6]
    Lottery4[1] = [34, 22]
    Lottery4[2] = [22, 34]
    Lottery4[3] = [30, 14]
    Lottery4[4] = [10, 50]

    # array for the fith lottery:
    
    Lottery5[0] = [20, 40]
    Lottery5[1] = [70, 10]
    Lottery5[2] = [27, 13]
    Lottery5[3] = [60, 4]
    Lottery5[4] = [14, 30]

    # array for the fith lottery:
    Lottery6[0] = [34, 33]
    Lottery6[1] = [50, 10]
    Lottery6[2] = [3, 91]
    Lottery6[3] = [10, 18]
    Lottery6[4] = [4, 60]

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
    # prolific ID:
    ProlificID = models.StringField()

    # token earnings from the experment
    earnings = models.IntegerField()

    # defining the shares for the different assets:
    portfolio_shares_a1 = models.IntegerField(initial=0)
    portfolio_shares_a2 = models.IntegerField(initial=0)
    portfolio_shares_a3 = models.IntegerField(initial=0)
    portfolio_shares_a4 = models.IntegerField(initial=0)
    portfolio_shares_a5 = models.IntegerField(initial=0)
    portfolio_shares_a6 = models.IntegerField(initial=0)
    tokens = models.IntegerField(initial=C.TOKEN_BUDGET)

    payment_round = models.IntegerField()

    # final investment
    final_choice_a1 = models.FloatField()
    final_choice_a2 = models.FloatField()
    final_choice_a3 = models.FloatField()
    final_choice_a4 = models.FloatField()
    final_choice_a5 = models.FloatField()
    final_choice_a6 = models.FloatField()

    # state of the world
    state_of_the_world = models.BooleanField(initial=False)

    # index of the budget subejct is facing
    budget_index = models.IntegerField(min=0,max=4)

    # final budget index:
    final_budget_index = models.IntegerField(min=0,max=4)


#-----------------------------------------------
# METHODS
#-----------------------------------------------
def creating_session(subsession):
    import random
    for p in subsession.get_players():
        set_order(p)


def set_order(player: Player):
    budget_indicies=[0,1,2,3,4]
    random.shuffle(budget_indicies)
    print(budget_indicies)
    players = player.in_all_rounds()

    i=0
    for p in players:
        p.budget_index = budget_indicies[i]
        i=i+1


def set_payoffs(player: Player):
    player.payment_round = random.randint(1,C.NUM_ROUNDS)
    p = player.in_round(player.payment_round)
    choice = [0 for i in range(0,5)]
    
    choice = [p.portfolio_shares_a1, p.portfolio_shares_a2, p.portfolio_shares_a3, p.portfolio_shares_a4, p.portfolio_shares_a5, p.portfolio_shares_a6]
    
    player.final_budget_index = p.budget_index

    player.final_choice_a1 = choice[0]
    player.final_choice_a2 = choice[1]
    player.final_choice_a3 = choice[2]
    player.final_choice_a4 = choice[3]
    player.final_choice_a5 = choice[4]
    player.final_choice_a6 = choice[5]

    r = random.uniform(0,1)
    
    lottery_payoffs = [0 for i in range(0,6)]
    if r<C.P_HEADS:
        player.state_of_the_world = True
        lottery_payoffs = [C.Lottery1[player.final_budget_index][0], C.Lottery2[player.final_budget_index][0], C.Lottery3[player.final_budget_index][0], C.Lottery4[player.final_budget_index][0], C.Lottery5[player.final_budget_index][0], C.Lottery6[player.final_budget_index][0]]
    else:
        player.state_of_the_world = False
        lottery_payoffs = [C.Lottery1[player.final_budget_index][1], C.Lottery2[player.final_budget_index][1], C.Lottery3[player.final_budget_index][1], C.Lottery4[player.final_budget_index][1], C.Lottery5[player.final_budget_index][1], C.Lottery6[player.final_budget_index][1]]

    temp = 0
    temp2 = 0
    for i in range(0,6):
        temp2 = temp2+choice[i]*lottery_payoffs[i]
        temp = temp+choice[i]*lottery_payoffs[i]/(C.EXCHANGE_RATE)

    player.earnings = temp2
    player.payoff = temp




#--------------------------------------------
# PAGES
#--------------------------------------------
class Welcome(Page):
    template_name = '_static/templates/Welcome.html'
    def is_displayed(player):
        return player.round_number == 1

class DecisionScreen(Page):
    template_name = '_static/templates/Complex_DecisionScreen.html'
    form_model = 'player'
    form_fields = ['tokens', 'portfolio_shares_a1', 'portfolio_shares_a2', 'portfolio_shares_a3', 'portfolio_shares_a4', 'portfolio_shares_a5', 'portfolio_shares_a6']

    @staticmethod
    def vars_for_template(player):
        i = player.budget_index
        return dict(
            lottery_1 = C.Lottery1[i],
            lottery_2 = C.Lottery2[i],
            lottery_3 = C.Lottery3[i],
            lottery_4 = C.Lottery4[i],
            lottery_5 = C.Lottery5[i],
            lottery_6 = C.Lottery6[i],
            )

    def error_message(player, values):
        if values['tokens']>0:
            return 'Please spend the entire budget'
        temp = values['portfolio_shares_a1']+values['portfolio_shares_a2']+values['portfolio_shares_a3']+values['portfolio_shares_a4']+values['portfolio_shares_a5']+values['portfolio_shares_a6']
        if temp>100:
            return 'Please reset the choice and make sure to meet the budget constaint'


    def before_next_page(player, timeout_happened):
        if player.subsession.round_number == C.NUM_ROUNDS:
            set_payoffs(player)

class ProlificID(Page):
    form_model = 'player'
    form_fields = ['ProlificID']
    template_name = '_static/templates/ProlificID.html'
    def is_displayed(player):
        return player.subsession.round_number == C.NUM_ROUNDS

class Results(Page):
#    template_name = '_static/templates/Complex_Results.html'

    def is_displayed(player):
        return player.subsession.round_number == C.NUM_ROUNDS

    @staticmethod
    def vars_for_template(player):
        i = player.final_budget_index
        return dict(
            lottery_1 = C.Lottery1[i],
            lottery_2 = C.Lottery2[i],
            lottery_3 = C.Lottery3[i],
            lottery_4 = C.Lottery4[i],
            lottery_5 = C.Lottery5[i],
            lottery_6 = C.Lottery6[i],
            state_of_the_world = player.state_of_the_world
            )
#--------------------------------------------



#--------------------------------------------
# PAGE SEQUENCE
#--------------------------------------------
page_sequence = [
                DecisionScreen,
                ProlificID,
                Results
                ]
