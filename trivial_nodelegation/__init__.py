from otree.api import *

import random


doc = """
Your app description
"""

# models
class C(BaseConstants):
    NAME_IN_URL = 'trivial_nodelegation'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 5

    # setting the exchange rate:
    EXCHANGE_RATE = .1
    
    # Probability of HEADS:
    P_HEADS = .5

    # Number of experts to be used
    NUM_OF_EXPERTS = 4

    # defining lotteries:
    # array for the first lottery:
    Lottery1 = [[0 for i in range(0,5)] for i in range(0,5)]

    Lottery1[0] = [100, 0]
    Lottery1[1] = [90, 10]
    Lottery1[2] = [80, 20]
    Lottery1[3] = [70, 30]
    Lottery1[4] = [60, 40]

    # array for the second lottery:
    Lottery2 = [[0 for i in range(0,5)] for i in range(0,5)]
    Lottery2[0] = [0, 100]
    Lottery2[1] = [10, 90]
    Lottery2[2] = [20, 80]
    Lottery2[3] = [30, 70]
    Lottery2[4] = [40, 60]



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # index of the budget subejct is facing
    budget_index = models.IntegerField(min=0,max=4)

    # lottery choice:
    lottery_choice = models.IntegerField(min=1,max=2)

    # payment round
    payment_round = models.IntegerField(min=1,max=C.NUM_ROUNDS)

    # final choice:
    final_choice = models.IntegerField(initial=0)

    # final budget index:
    final_budget_index = models.IntegerField(min=0,max=4)

    # state of the world
    state_of_the_world = models.BooleanField(initial=False)



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
    
    choice = p.lottery_choice
    budget_index = p.budget_index

    player.final_choice = choice
    player.final_budget_index = budget_index
    r = random.uniform(0,1)
    if choice == 1:
        if r<C.P_HEADS:
            player.state_of_the_world = True
            payoff = C.Lottery1[budget_index][0]
        else:
            player.state_of_the_world = False
            payoff = C.Lottery1[budget_index][1]
    if choice == 2:
        if r<C.P_HEADS:
            player.state_of_the_world = True
            payoff = C.Lottery2[budget_index][0]
        else:
            player.state_of_the_world = False
            payoff = C.Lottery2[budget_index][1]

    player.payoff = cu(payoff)*C.EXCHANGE_RATE





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
        i = player.budget_index
        return dict(
            lottery_1 = C.Lottery1[i],
            lottery_2 = C.Lottery2[i],
            )
         
    def before_next_page(player, timeout_happened):
        if player.subsession.round_number == C.NUM_ROUNDS:
            set_payoffs(player)

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
        i = player.final_budget_index
        return dict(
            lottery_1 = C.Lottery1[i],
            lottery_2 = C.Lottery2[i],
            state_of_the_world = player.state_of_the_world
            )


page_sequence = [
#                Welcome,
                DecisionScreen,
#                ResultsComputePage, 
                Results
                ]



