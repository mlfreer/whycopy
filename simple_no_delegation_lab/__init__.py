from otree.api import *

import random

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'simple_lab'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    NUM_ROUNDS = 5

    # Probability of HEADS:
    P_HEADS = .5

    # showup fee
    SHOWUP_FEE = cu(4)

    # QUIZ VARIABLES:
    ANSWER1 = 30
    ANSWER2 = 1

    # Tokens budget:
    EXCHANGE_RATE = 20

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

    # array for the sixth lottery:
    Lottery6[0] = [34, 33]
    Lottery6[1] = [50, 10]
    Lottery6[2] = [3, 91]
    Lottery6[3] = [10, 18]
    Lottery6[4] = [4, 60]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # token earnings from the experment
    earnings = models.IntegerField()

    # defining the shares for the different assets:
    lottery_choice = models.IntegerField(min=1,max=6)

    payment_round = models.IntegerField()

    # final investment
    final_choice = models.IntegerField(min=1,max=6)

    # state of the world
    state_of_the_world = models.BooleanField(initial=False)

    # index of the budget subejct is facing
    budget_index = models.IntegerField(min=0,max=4)

    # final budget index:
    final_budget_index = models.IntegerField(min=0,max=4)

    #quiz variables:
    question1 = models.IntegerField(min=0,max=1000)
    question2 = models.IntegerField(min=0,max=1000)

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
    if choice == 3:
        if r<C.P_HEADS:
            player.state_of_the_world = True
            payoff = C.Lottery3[budget_index][0]
        else:
            player.state_of_the_world = False
            payoff = C.Lottery3[budget_index][1]
    if choice == 4:
        if r<C.P_HEADS:
            player.state_of_the_world = True
            payoff = C.Lottery4[budget_index][0]
        else:
            player.state_of_the_world = False
            payoff = C.Lottery4[budget_index][1]
    if choice == 5:
        if r<C.P_HEADS:
            player.state_of_the_world = True
            payoff = C.Lottery5[budget_index][0]
        else:
            player.state_of_the_world = False
            payoff = C.Lottery5[budget_index][1]
    if choice == 6:
        if r<C.P_HEADS:
            player.state_of_the_world = True
            payoff = C.Lottery6[budget_index][0]
        else:
            player.state_of_the_world = False
            payoff = C.Lottery6[budget_index][1]

    player.earnings=round(payoff,1)
    player.payoff = round(cu(payoff)/C.EXCHANGE_RATE + C.SHOWUP_FEE,1)


# PAGES
class ConsentForm(Page):
    def is_displayed(player):
        return player.subsession.round_number == 1

class InstructionsOverview(Page):
    def is_displayed(player):
        return player.subsession.round_number == 1

class Instructions(Page):
    def is_displayed(player):
        return player.subsession.round_number == 1

class Welcome(Page):
    def is_displayed(player):
        return player.subsession.round_number == 1

class Question1(Page):
    def is_displayed(player):
        return player.subsession.round_number == 1

    form_model = 'player'
    form_fields = ['question1']

    def error_message(player, value):
        if value['question1'] != C.ANSWER1:
            result = 'Wrong Answer. Please Try Again.'
            return result
            

class Question2(Page):
    def is_displayed(player):
        return player.subsession.round_number == 1

    form_model = 'player'
    form_fields = ['question2']

    def error_message(player, value):
        if value['question2'] != C.ANSWER2:
            result = 'Wrong Answer. Please Try Again. You have ' + str(left)+ ' attempts left.'
            return result
            

class Success(Page):
    def is_displayed(player):
        return player.subsession.round_number == 1
    



class DecisionScreen(Page):
    template_name = '_static/templates/Simple_DecisionScreen.html'
    form_model = 'player'
    form_fields = ['lottery_choice']

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
         
    def before_next_page(player, timeout_happened):
        if player.subsession.round_number == C.NUM_ROUNDS:
            set_payoffs(player)


class Results(Page):
    def is_displayed(player):
        return player.subsession.round_number == C.NUM_ROUNDS

    @staticmethod
    def vars_for_template(player):
        i = player.final_budget_index
        temp = player.payoff-C.SHOWUP_FEE
        return dict(
            lottery_1 = C.Lottery1[i],
            lottery_2 = C.Lottery2[i],
            lottery_3 = C.Lottery3[i],
            lottery_4 = C.Lottery4[i],
            lottery_5 = C.Lottery5[i],
            lottery_6 = C.Lottery6[i],
            earnings = temp,
            state_of_the_world = player.state_of_the_world,
            )



page_sequence = [
                ConsentForm,
                InstructionsOverview,
                Instructions,
                Welcome,
                Question1,
                Question2,
                Success,
                DecisionScreen,
                Results
                ]