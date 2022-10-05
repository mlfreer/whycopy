from otree.api import *
import random


doc = """
Your app description
"""

#------------------------------------------------------------
# CONSTANTS
#------------------------------------------------------------
class C(BaseConstants):
    NAME_IN_URL = 'no_delegation'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 15
    BLOCK_SIZE = 5

    EXCHANGE_RATE = 20;

    # Probability of HEADS:
    P_HEADS = .5

    # simple and complex lotteries
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

    # trivial lotteries:
    # array for the first lottery:
    trivial_Lottery1 = [[0 for i in range(0,5)] for i in range(0,5)]

    trivial_Lottery1[0] = [100, 0]
    trivial_Lottery1[1] = [90, 10]
    trivial_Lottery1[2] = [80, 20]
    trivial_Lottery1[3] = [70, 30]
    trivial_Lottery1[4] = [60, 40]

    # array for the second lottery:
    trivial_Lottery2 = [[0 for i in range(0,5)] for i in range(0,5)]
    trivial_Lottery2[0] = [0, 100]
    trivial_Lottery2[1] = [10, 90]
    trivial_Lottery2[2] = [20, 80]
    trivial_Lottery2[3] = [30, 70]
    trivial_Lottery2[4] = [40, 60]

#------------------------------------------------------------
# CLASSES
#------------------------------------------------------------
class Subsession(BaseSubsession):  
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    #------------------------------------------------------------
    # treatment independent variables
    treatment_index = models.IntegerField(min=0,max=2)
    budget_index = models.IntegerField(min=0,max=2)
    earnings = models.IntegerField(initial=0)
    payment_block = models.IntegerField(min=0,max=2)
    payment_round = models.IntegerField(min=1,max=4)
    state_of_the_world = models.BooleanField(initial=False)
    #------------------------------------------------------------

    #------------------------------------------------------------
    # complex treatments variables:
    # decision variables
    complex_shares_1 = models.FloatField()
    complex_shares_2 = models.FloatField()
    complex_shares_3 = models.FloatField()
    complex_shares_4 = models.FloatField()
    complex_shares_5 = models.FloatField()
    complex_shares_6 = models.FloatField()
    tokens = models.FloatField()
    complex_final_budget_index = models.IntegerField(min=0,max=4)
    # state of the world
    #------------------------------------------------------------

    #------------------------------------------------------------
    # simple treatment variables
    # choice variables
    simple_lottery_choice =  models.IntegerField(min=1,max=6)
    # state of the world
    #------------------------------------------------------------

    #------------------------------------------------------------
    # trivial treatment variables
    # choice variables
    trivial_lottery_choice =  models.IntegerField(min=1,max=6)
    # state of the world
    #------------------------------------------------------------


#------------------------------------------------------------
# GLOBAL FUNCTIONS
#------------------------------------------------------------
# creating treatment order
def creating_session(subsession):
    import random
    # start with creating random treatment order at the player level 
    for p in subsession.get_players():
        set_treatment_order(p)
        set_trivial_budgets(p)
        set_simple_budgets(p)
        set_complex_budgets(p)


def set_treatment_order(player: Player):
    #------------------------------------------------------------
    indicies=[0,1,2]
    random.shuffle(indicies)
    players = player.in_all_rounds()
    #------------------------------------------------------------

    # mulitplying the array
    temp = [0 for i in range(0,15)] 
    for i in range(0,15):
        if i<= 4:
            temp[i] = indicies[0]
        else:
            if i<=9:
                temp[i] = indicies[1]
            else:
                temp[i] = indicies[2]
    #------------------------------------------------------------

    i=0
    for p in players:
        p.treatment_index = temp[i]
        i=i+1
    #------------------------------------------------------------


def set_trivial_budgets(player: Player):
    budget_indicies=[0,1,2,3,4]
    random.shuffle(budget_indicies)
#    print(budget_indicies)
    players = player.in_all_rounds()
    #------------------------------------------------------------

    i=0
    j=0
    for p in players:
        if p.treatment_index == 0:
            p.budget_index = budget_indicies[j]
            j=j+1
        i=i+1
    #------------------------------------------------------------

def set_simple_budgets(player: Player):
    budget_indicies=[0,1,2,3,4]
    random.shuffle(budget_indicies)
#    print(budget_indicies)
    players = player.in_all_rounds()
    #------------------------------------------------------------
    
    i=0
    j=0
    for p in players:
        if p.treatment_index == 1:
            p.budget_index = budget_indicies[j]
            j=j+1
        i=i+1
    #------------------------------------------------------------

def set_complex_budgets(player: Player):
    budget_indicies=[0,1,2,3,4]
    random.shuffle(budget_indicies)
#    print(budget_indicies)
    players = player.in_all_rounds() 
    #------------------------------------------------------------
    
    i=0
    j=0
    for p in players:
        if p.treatment_index == 2:
            p.budget_index = budget_indicies[j]
            j=j+1
        i=i+1
    #------------------------------------------------------------

def set_payoffs(player: Player):
    player.payment_block = random.randint(0,2)
    payment_round = random.randint(1,4)
    player.payment_round = player.payment_block*5 + payment_round
    p = player.in_round(player.payment_round)
    player.earnings = 0
    #------------------------------------------------------------

    # by the time the payment_round.
    first_payment_round = player.payment_round
    second_payment_round = player.payment_block*5 + 5

    if p.treatment_index==0:
        set_trivial_payoffs(player,first_payment_round)
        set_trivial_payoffs(player,second_payment_round)
    elif p.treatment_index==1:
        set_simple_payoffs(player,first_payment_round)
        set_simple_payoffs(player,second_payment_round)
    elif p.treatment_index==2:
        set_complex_payoffs(player,first_payment_round)
        set_complex_payoffs(player,second_payment_round)
    #------------------------------------------------------------
    player.payoff = cu(player.earnings)/C.EXCHANGE_RATE

def set_trivial_payoffs(player: Player, round):
    p = player.in_round(round) # getting player in given round
    choice = p.trivial_lottery_choice # retrieving player's choice
    budget_index = p.budget_index # retrieving budget index
    r = random.uniform(0,1) # generating  state of the world
    #------------------------------------------------------------

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
    player.earnings=player.earnings + payoff
#----------------------------------------------------------------

def set_simple_payoffs(player: Player, round):
    p = player.in_round(round)
    
    choice = p.simple_lottery_choice
    budget_index = p.budget_index

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

    player.earnings=player.earnings + payoff
#----------------------------------------------------------------


def set_complex_payoffs(player: Player, round):
    choice = [0 for i in range(0,5)]
    
    choice = [p.complex_shares_1, p.complex_shares_2, p.complex_shares_3, p.complex_shares_4, p.complex_shares_5, p.complex_shares_6]
    
    final_budget_index = p.budget_index
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
    #----------------------------------------------------------------
    player.earnings = player.earnings+temp2
#----------------------------------------------------------------


#------------------------------------------------------------
# PAGES
#------------------------------------------------------------
class Trivial_Instructions(Page):
    def is_displayed(player):
        return player.treatment_index==0 and player.subsession.round_number % C.BLOCK_SIZE == 1
    template_name = '_static/templates/Trivial_Instructions.html'
    #------------------------------------------------------------

class Simple_Instructions(Page):
    def is_displayed(player):
        return player.treatment_index==1 and player.subsession.round_number % C.BLOCK_SIZE == 1
    template_name = '_static/templates/Simple_Instructions.html'
    #------------------------------------------------------------

class Complex_Instructions_P1(Page):
    def is_displayed(player):
        return player.treatment_index==2 and player.subsession.round_number % C.BLOCK_SIZE == 1
    template_name = '_static/templates/Complex_InstructionsPage1.html'
    #------------------------------------------------------------

class Complex_Instructions_P2(Page):
    def is_displayed(player):
        return player.treatment_index==2 and player.subsession.round_number % C.BLOCK_SIZE == 1
    template_name = '_static/templates/Complex_InstructionsPage2.html'
    #------------------------------------------------------------

class Complex_Instructions_P3(Page):
    def is_displayed(player):
        return player.treatment_index==2 and player.subsession.round_number % C.BLOCK_SIZE == 1
    template_name = '_static/templates/Complex_InstructionsPage3.html'
    #------------------------------------------------------------


class Trivial_DecisionScreen(Page):
    def is_displayed(player):
        return player.treatment_index==0

    template_name = '_static/templates/Trivial_DecisionScreen.html'
    form_model = 'player'
    form_fields = ['trivial_lottery_choice']

    @staticmethod
    def vars_for_template(player):
        i = player.budget_index
        return dict(
            lottery_1 = C.trivial_Lottery1[i],
            lottery_2 = C.trivial_Lottery2[i],
            )
         
    def before_next_page(player, timeout_happened):
        if player.subsession.round_number == C.NUM_ROUNDS:
            set_payoffs(player)
    #------------------------------------------------------------



class Simple_DecisionScreen(Page):
    def is_displayed(player):
        return player.treatment_index==1

    template_name = '_static/templates/Simple_DecisionScreen.html'
    form_model = 'player'
    form_fields = ['simple_lottery_choice']

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
    #------------------------------------------------------------

class Complex_DecisionScreen(Page):
    def is_displayed(player):
        return player.treatment_index == 2

    template_name = '_static/templates/Complex_DecisionScreen.html'
    form_model = 'player'
    form_fields = ['tokens', 'complex_shares_1', 'complex_shares_2', 'complex_shares_3', 'complex_shares_4', 'complex_shares_5','complex_shares_6']

    @staticmethod
    def vars_for_template(player):
        i = player.budget_index
        return dict(
            lottery_1 = C.Lottery1[i],
            lottery_2 = C.Lottery2[i],
            lottery_3 = C.Lottery3[i],
            lottery_4 = C.Lottery4[i],
            lottery_5 = C.Lottery5[i],
            lottery_6 = C.Lottery5[i],
            )

    def error_message(player, values):
        if values['tokens']>0:
            return 'Please spend the entire budget'

    def before_next_page(player, timeout_happened):
        if player.subsession.round_number == C.NUM_ROUNDS:
            set_payoffs(player)
    #------------------------------------------------------------

class Results(Page):
    def is_displayed(player):
        return player.subsession.round_number == C.NUM_ROUNDS
    template_name = '_static/templates/NoDelegation_Results.html'

    @staticmethod
    def vars_for_template(player):
        i = player.budget_index
        return dict(
            first_payment_round = player.payment_round,
            second_payment_round = player.payment_block*5 + 5,
            payment_block = player.payment_block + 1
            )


#------------------------------------------------------------
# PAGE SEQUENCE
#------------------------------------------------------------
page_sequence = [Trivial_Instructions,
                Trivial_DecisionScreen,
                Simple_Instructions,
                Simple_DecisionScreen,
                Complex_Instructions_P1,
                Complex_Instructions_P2,
                Complex_Instructions_P3,
                Complex_DecisionScreen,
                Results
                ]
