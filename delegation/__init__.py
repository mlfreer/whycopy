from otree.api import *
import random
import math

doc = """
Your app description
"""

#------------------------------------------------------------
# CONSTANTS
#------------------------------------------------------------
class C(BaseConstants):
    NAME_IN_URL = 'delegation'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 15
    BLOCK_SIZE = 5

    PARTICIPATION_FEE = cu(1.5)

    EXCHANGE_RATE = 20;

    DELEGATION_COSTS = cu(0.10)

    #------------------------------------------------------------
    # QUIZ ANSWERS:
    MAX_ATTEMPTS = 3

    TRIVIAL_ANSWER1 = 30
    TRIVIAL_ANSWER2 = 4

    SIMPLE_ANSWER1 = 30
    SIMPLE_ANSWER2 = 1

    COMPLEX_ANSWER1 = 3
    COMPLEX_ANSWER2 = 2
    #------------------------------------------------------------

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
    # EXPERTS
    NUM_EXPERTS = 5
    E_PAYMENTS = [2.5, 2.9, 3.5, 4.6, 8.5] # earnings in the experiment
    E_QUALITY = [1, 1, 1, 0, 0] # quality rating
    E_RISK = [1, 2, 3, 2, 3] # risk rating
    #------------------------------------------------------------

    #------------------------------------------------------------
    # EXPERT CHOICES
    #------------------------------------------------------------
    # TRIVIAL CHOICES:
    E_TRIVIAL_CHOICES = [[0 for i in range(0,5)] for i in range(0,5)]
    E_TRIVIAL_CHOICES[0] = [1, 2, 2, 2, 2]
    E_TRIVIAL_CHOICES[1] = [1, 2, 2, 1, 1]
    E_TRIVIAL_CHOICES[2] = [1, 2, 1, 2, 1]
    E_TRIVIAL_CHOICES[3] = [1, 1,     1,     2,     1]
    E_TRIVIAL_CHOICES[4] = [1,     1,     1,     1,     1]


    # SIMPLE CHOICES:
    E_SIMPLE_CHOICES = [[0 for i in range(0,5)] for i in range(0,5)]
    E_SIMPLE_CHOICES[0] = [3, 4, 1, 4, 1]
    E_SIMPLE_CHOICES[1] = [2, 1, 3, 1, 3]
    E_SIMPLE_CHOICES[2] = [3, 3, 1, 3, 3]
    E_SIMPLE_CHOICES[3] = [1, 1, 1, 2, 1]
    E_SIMPLE_CHOICES[4] = [3, 6, 1, 5, 5]


    # COMPLEX CHOICES:
    E_COMPLEX_CHOICES = [[[0 for i in range(0,6)] for i in range(0,6)] for i in range(0,6)]

    # EXPERT 1:
    E_COMPLEX_CHOICES[0][0] = [0.3400,    0.3400,    0.1800,    0.1100,    0.3400]
    E_COMPLEX_CHOICES[0][1] = [0,         0,    0.3800,    0.1900,         0]
    E_COMPLEX_CHOICES[0][2] = [0,         0,    0.2900,    0.0100,         0]
    E_COMPLEX_CHOICES[0][3] = [0.3800,    0.3800,    0.1500,    0.2500,    0.3800]
    E_COMPLEX_CHOICES[0][4] = [0.2800,    0.2800,         0,    0.2000,    0.2800]
    E_COMPLEX_CHOICES[0][5] = [0,         0,         0,    0.2400,         0]

    # EXPERT 2:
    E_COMPLEX_CHOICES[1][0] = [0.1000, 0.1000,    0.2000,    0.2100,    0.1000]
    E_COMPLEX_CHOICES[1][1] = [0.2000,    0.2000,   0.1500,    0.1400,   0.2000]
    E_COMPLEX_CHOICES[1][2] = [0.1500,    0.1500,    0.1500,    0.1800,    0.1500]
    E_COMPLEX_CHOICES[1][3] = [0.2000,    0.2000,    0.2000,    0.1000,    0.2000]
    E_COMPLEX_CHOICES[1][4] = [0.1500,    0.1500,   0.1400,    0.1800,    0.1500]
    E_COMPLEX_CHOICES[1][5] = [0.2000,    0.2000,    0.1600,    0.1900,    0.2000]


    # EXPERT 3:
    E_COMPLEX_CHOICES[2][0] = [0,         0,         0,    0.4000,         0]
    E_COMPLEX_CHOICES[2][1] = [0,         0,         0,    0.1500,         0]
    E_COMPLEX_CHOICES[2][2] = [1.0000,    1.0000,    0,    0.1500,    1.0000]
    E_COMPLEX_CHOICES[2][3] = [0,         0,    0.5000,         0,         0]
    E_COMPLEX_CHOICES[2][4] = [0,         0,         0,    0.1500,         0]
    E_COMPLEX_CHOICES[2][5] = [0,         0,    0.5000,    0.1500,         0]

    # EXPERT 4:
    E_COMPLEX_CHOICES[3][0] = [0.0800,    0.1400,    0.6700,    0.1400,    0.6700]
    E_COMPLEX_CHOICES[3][1] = [0.2400,    0.1300,    0.3300,    0.1300,    0.3300]
    E_COMPLEX_CHOICES[3][2] = [0.3100,    0.2000,         0,    0.2000,         0]
    E_COMPLEX_CHOICES[3][3] = [0.1500,    0.1000,         0,    0.1000,         0]
    E_COMPLEX_CHOICES[3][4] = [0.0900,    0.1500,         0,    0.1500,         0]
    E_COMPLEX_CHOICES[3][5] = [0.1300,    0.2800,         0,    0.2800,         0]

    # EXPERT 5:
    E_COMPLEX_CHOICES[4][0] = [0,    1.0000,         0,    1.0000,         0]
    E_COMPLEX_CHOICES[4][1] = [0,         0,         0,         0,         0]
    E_COMPLEX_CHOICES[4][2] = [0.4000,    0,    0.2000,         0,    0.2000]
    E_COMPLEX_CHOICES[4][3] = [0,         0,         0,         0,         0]
    E_COMPLEX_CHOICES[4][4] = [0.2000,    0,         0,         0,         0]
    E_COMPLEX_CHOICES[4][5] = [0.4000,    0,    0.8000,         0,    0.8000]
    #------------------------------------------------------------


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
    budget_index = models.IntegerField(min=0,max=5)
    earnings = models.FloatField(default=0)
    payment_block = models.IntegerField(min=0,max=2)
    payment_round = models.IntegerField(min=1,max=4)
    state_of_the_world = models.BooleanField(initial=False)

    return_study = models.BooleanField(initial=False)

    # first period earnings
    earnings_period_one = models.CurrencyField()
    earnings_period_two = models.CurrencyField()

    # prolific ID:
    ProlificID = models.StringField()
    #------------------------------------------------------------

    #------------------------------------------------------------
    # expert indexes:
    expert_index_1 = models.IntegerField(min=0,max=5)
    expert_index_2 = models.IntegerField(min=0,max=5)
    expert_index_3 = models.IntegerField(min=0,max=5)
    expert_index_4 = models.IntegerField(min=0,max=5)
    expert_index_5 = models.IntegerField(min=0,max=5)
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
    # delegation decisions
    trivial_delegation = models.IntegerField(min=-2,max=5,initial=-2)
    simple_delegation = models.IntegerField(min=-2,max=5,initial=-2)
    complex_delegation = models.IntegerField(min=-2,max=5,initial=-2)
    delegation_decision = models.IntegerField(min=0,max=1,initial=0)
    #------------------------------------------------------------

    #------------------------------------------------------------
    # trivial quiz:
    trivial_attempts_1 = models.IntegerField(min=0, max=10, initial=0)
    trivial_attempts_2 = models.IntegerField(min=0, max=10, initial=0)

    trivial_question_1 = models.IntegerField(min=0,max=1000)
    trivial_question_2 = models.IntegerField(min=0,max=1000)
    #------------------------------------------------------------

    #------------------------------------------------------------
    # simple quiz:
    simple_attempts_1 = models.IntegerField(min=0, max=10, initial=0)
    simple_attempts_2 = models.IntegerField(min=0, max=10, initial=0)

    simple_question_1 = models.IntegerField(min=0,max=1000)
    simple_question_2 = models.IntegerField(min=0,max=1000)
    #------------------------------------------------------------

    #------------------------------------------------------------
    # complex quiz:
    complex_attempts_1 = models.IntegerField(min=0, max=10, initial=0)
    complex_attempts_2 = models.IntegerField(min=0, max=10, initial=0)

    complex_question_1 = models.IntegerField(min=0,max=1000)
    complex_question_2 = models.IntegerField(min=0,max=1000)
    #------------------------------------------------------------


    #------------------------------------------------------------
    # BIG5 Questionnaire
    #------------------------------------------------------------
    big5_reserved = models.IntegerField(min=0,max=5, initial=0)
    big5_trusting = models.IntegerField(min=0,max=5, initial=0)
    big5_lazy = models.IntegerField(min=0,max=5, initial=0)
    big5_relaxed = models.IntegerField(min=0,max=5, initial=0)
    big5_artistic = models.IntegerField(min=0,max=5, initial=0)
    big5_outgoing = models.IntegerField(min=0,max=5, initial=0)
    big5_blameshifting = models.IntegerField(min=0,max=5, initial=0)
    big5_job = models.IntegerField(min=0,max=5, initial=0)
    big5_nervuous = models.IntegerField(min=0,max=5, initial=0)
    big5_imagination = models.IntegerField(min=0,max=5, initial=0)
    big5_considerate = models.IntegerField(min=0,max=5, initial=0)


    #------------------------------------------------------------
    # Risk TOLERANCE QUESTIONNAIRE
    #------------------------------------------------------------
    risk_general = models.IntegerField(min=0,max=5,initial=0)
    risk_financial = models.IntegerField(min=0,max=5,initial=0)
    risk_investment = models.IntegerField(min=0,max=5,initial=0)
    risk_responsibility = models.IntegerField(min=0,max=5,initial=0)

    #------------------------------------------------------------
    # WTP for delegation
    #------------------------------------------------------------
    wtp_delegation = models.CurrencyField(label="")

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
        set_experts_index(p)
        set_payment_round(p)


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

def set_experts_index(player: Player):
    expert_index = [0,1,2,3,4]
    random.shuffle(expert_index)
    players = player.in_all_rounds()

    for p in players:
        p.expert_index_1 = expert_index[0]
        p.expert_index_2 = expert_index[1]
        p.expert_index_3 = expert_index[2]
        p.expert_index_4 = expert_index[3]
        p.expert_index_5 = expert_index[4]
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

def set_payment_round(player: Player):
    player.payment_block = random.randint(0,2)
    payment_round = random.randint(1,4)
    player.payment_round = player.payment_block*5 + payment_round

    for p in player.in_all_rounds():
        p.payment_block = player.payment_block
        p.payment_round = player.payment_round

def set_payoffs(player: Player):
    p = player.in_round(player.payment_round)
    player.earnings = 0
    #------------------------------------------------------------

    # by the time the payment_round.
    first_payment_round = player.payment_round
    second_payment_round = player.payment_block*5 + 5
    player.payoff = cu(0)

    if p.treatment_index==0:
        set_trivial_payoffs(player,first_payment_round)
        player.earnings_period_one = cu(player.earnings/C.EXCHANGE_RATE)
        set_trivial_payoffs(player,second_payment_round)
        player.earnings_period_two = cu(player.earnings/C.EXCHANGE_RATE - player.earnings_period_one)
        if player.trivial_delegation>=0:
            player.payoff = player.payoff - C.DELEGATION_COSTS
            player.delegation_decision = 1

    elif p.treatment_index==1:
        set_simple_payoffs(player,first_payment_round)
        player.earnings_period_one = cu(player.earnings/C.EXCHANGE_RATE)
        set_simple_payoffs(player,second_payment_round)
        player.earnings_period_two = cu(player.earnings/C.EXCHANGE_RATE - player.earnings_period_one)
        if player.simple_delegation>=0:
            player.payoff = player.payoff - C.DELEGATION_COSTS
            player.delegation_decision = 1

    elif p.treatment_index==2:
        set_complex_payoffs(player,first_payment_round)
        player.earnings_period_one = cu(player.earnings/C.EXCHANGE_RATE)
        set_complex_payoffs(player,second_payment_round)
        player.earnings_period_two = cu(player.earnings/C.EXCHANGE_RATE - player.earnings_period_one)
        if player.complex_delegation>=0:
            player.payoff = player.payoff - C.DELEGATION_COSTS
            player.delegation_decision = 1

    #------------------------------------------------------------
    player.payoff = player.payoff+cu(player.earnings)/C.EXCHANGE_RATE

def set_trivial_payoffs(player: Player, round):
    p = player.in_round(round) # getting player in given round
    choice = p.trivial_lottery_choice # retrieving player's choice
    budget_index = p.budget_index # retrieving budget index
    r = random.uniform(0,1) # generating  state of the world
    #------------------------------------------------------------

    if choice == 1:
        if r<C.P_HEADS:
            player.state_of_the_world = True
            payoff = C.trivial_Lottery1[budget_index][0]
        else:
            player.state_of_the_world = False
            payoff = C.trivial_Lottery1[budget_index][1]
    if choice == 2:
        if r<C.P_HEADS:
            player.state_of_the_world = True
            payoff = C.trivial_Lottery2[budget_index][0]
        else:
            player.state_of_the_world = False
            payoff = C.trivial_Lottery2[budget_index][1]
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
    p = player.in_round(round)
    choice = [p.complex_shares_1, p.complex_shares_2, p.complex_shares_3, p.complex_shares_4, p.complex_shares_5, p.complex_shares_6]
    
    final_budget_index = p.budget_index
    r = random.uniform(0,1)
    
    lottery_payoffs = [0 for i in range(0,6)]
    if r<C.P_HEADS:
        player.state_of_the_world = True
        lottery_payoffs = [C.Lottery1[final_budget_index][0], C.Lottery2[final_budget_index][0], C.Lottery3[final_budget_index][0], C.Lottery4[final_budget_index][0], C.Lottery5[final_budget_index][0], C.Lottery6[final_budget_index][0]]
    else:
        player.state_of_the_world = False
        lottery_payoffs = [C.Lottery1[final_budget_index][1], C.Lottery2[final_budget_index][1], C.Lottery3[final_budget_index][1], C.Lottery4[final_budget_index][1], C.Lottery5[final_budget_index][1], C.Lottery6[final_budget_index][1]]

    temp = 0
    temp2 = 0
    for i in range(0,6):
        temp2 = temp2+choice[i]*lottery_payoffs[i]
    #----------------------------------------------------------------
    player.earnings = player.earnings+temp2/100
#----------------------------------------------------------------


#------------------------------------------------------------
# PAGES
#------------------------------------------------------------


#----------------------------------------------------------------
# INSTRUCTIONS
#----------------------------------------------------------------
class Trivial_Instructions(Page):
    def is_displayed(player):
        return player.treatment_index==0 and player.subsession.round_number % C.BLOCK_SIZE == 1
    template_name = '_static/templates/Trivial_Instructions.html'

    @staticmethod
    def vars_for_template(player):
        return dict(
            block_number = player.subsession.round_number // C.BLOCK_SIZE + 1
            )
    #------------------------------------------------------------

class Simple_Instructions(Page):
    def is_displayed(player):
        return player.treatment_index==1 and player.subsession.round_number % C.BLOCK_SIZE == 1
    template_name = '_static/templates/Simple_Instructions.html'

    @staticmethod
    def vars_for_template(player):
        return dict(
            block_number = player.subsession.round_number // C.BLOCK_SIZE + 1
            )
    #------------------------------------------------------------

class Complex_Instructions_P1(Page):
    def is_displayed(player):
        return player.treatment_index==2 and player.subsession.round_number % C.BLOCK_SIZE == 1
    template_name = '_static/templates/Complex_InstructionsPage1.html'

    @staticmethod
    def vars_for_template(player):
        return dict(
            block_number = player.subsession.round_number // C.BLOCK_SIZE + 1
            )
    #------------------------------------------------------------

class Complex_Instructions_P2(Page):
    def is_displayed(player):
        return player.treatment_index==2 and player.subsession.round_number % C.BLOCK_SIZE == 1
    template_name = '_static/templates/Complex_InstructionsPage2.html'

    @staticmethod
    def vars_for_template(player):
        return dict(
            block_number = player.subsession.round_number // C.BLOCK_SIZE + 1
            )
    #------------------------------------------------------------

class Complex_Instructions_P3(Page):
    def is_displayed(player):
        return player.treatment_index==2 and player.subsession.round_number % C.BLOCK_SIZE == 1
    template_name = '_static/templates/Complex_InstructionsPage3.html'

    @staticmethod
    def vars_for_template(player):
        return dict(
            block_number = player.subsession.round_number // C.BLOCK_SIZE + 1
            )
    #------------------------------------------------------------
#----------------------------------------------------------------


#----------------------------------------------------------------
# DECISION PAGES
#----------------------------------------------------------------
class Trivial_DecisionScreen(Page):
    def is_displayed(player):
        return (player.treatment_index==0 and player.subsession.round_number % C.BLOCK_SIZE != 0) or (player.treatment_index==0 and player.subsession.round_number % C.BLOCK_SIZE == 0 and player.trivial_delegation<=-1)

    template_name = '_static/templates/Trivial_DecisionScreen.html'
    form_model = 'player'
    form_fields = ['trivial_lottery_choice']

    @staticmethod
    def vars_for_template(player):
        i = player.budget_index
        return dict(
            lottery_1 = C.trivial_Lottery1[i],
            lottery_2 = C.trivial_Lottery2[i],
            residual = player.subsession.round_number % 5,
            )

    @staticmethod
    def before_next_page(player,timeout_happened):
        if player.subsession.round_number>1:
            p = player.in_round(player.subsession.round_number-1)
            if p.trivial_delegation>=-1:
                player.trivial_delegation=p.trivial_delegation
            if p.simple_delegation>=-1:
                player.simple_delegation = p.simple_delegation
            if p.complex_delegation>=-1:
                player.complex_delegation = p.complex_delegation
    #------------------------------------------------------------

class Simple_DecisionScreen(Page):
    def is_displayed(player):
        return (player.treatment_index==1 and player.subsession.round_number % C.BLOCK_SIZE != 0) or (player.treatment_index==1 and player.subsession.round_number % C.BLOCK_SIZE == 0 and player.simple_delegation<=-1)

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
            residual = player.subsession.round_number % 5,
            )

    @staticmethod
    def before_next_page(player,timeout_happened):
        if player.subsession.round_number>1:
            p = player.in_round(player.subsession.round_number-1)
            if p.trivial_delegation>=-1:
                player.trivial_delegation=p.trivial_delegation
            if p.simple_delegation>=-1:
                player.simple_delegation = p.simple_delegation
            if p.complex_delegation>=-1:
                player.complex_delegation = p.complex_delegation
    #------------------------------------------------------------

class Complex_DecisionScreen(Page):
    def is_displayed(player):
        return (player.treatment_index==2 and player.subsession.round_number % C.BLOCK_SIZE != 0) or (player.treatment_index==2 and player.subsession.round_number % C.BLOCK_SIZE == 0 and player.complex_delegation<=-1)

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
            lottery_6 = C.Lottery6[i],
            residual = player.subsession.round_number % 5,
            )

    def error_message(player, values):
        if values['tokens']>0:
            return 'Please spend the entire budget'

    @staticmethod
    def before_next_page(player,timeout_happened):
        if player.subsession.round_number>1:
            p = player.in_round(player.subsession.round_number-1)
            if p.trivial_delegation>=-1:
                player.trivial_delegation=p.trivial_delegation
            if p.simple_delegation>=-1:
                player.simple_delegation = p.simple_delegation
            if p.complex_delegation>=-1:
                player.complex_delegation = p.complex_delegation
    #------------------------------------------------------------
#----------------------------------------------------------------


#----------------------------------------------------------------
# QUIZZES
#----------------------------------------------------------------
class Trivial_Question1(Page):
    template_name = '_static/templates/Trivial_Question1.html'
    def is_displayed(player):
        return player.treatment_index==0 and player.subsession.round_number % C.BLOCK_SIZE == 1 and player.trivial_attempts_1 < C.MAX_ATTEMPTS

    form_model = 'player'
    form_fields = ['trivial_question_1']

    def error_message(player, value):
        if value['trivial_question_1'] != C.TRIVIAL_ANSWER1:
            player.trivial_attempts_1 = player.trivial_attempts_1 + 1
            left = C.MAX_ATTEMPTS - player.trivial_attempts_1
            
            if player.trivial_attempts_1 >= C.MAX_ATTEMPTS:
                player.return_study=True

            if player.trivial_attempts_1 < C.MAX_ATTEMPTS:
                result = 'Wrong Answer. Please Try Again. You have ' + str(left)+ ' attempts left.'
                return result
            else:
                result = 'Wrong Answer. The correct Answer is  ' + str(C.TRIVIAL_ANSWER1)+ '. Please input it to proceed.'
                return result


class Trivial_Question2(Page):
    template_name = '_static/templates/Trivial_Question2.html'
    def is_displayed(player):
        return player.treatment_index==0 and player.subsession.round_number % C.BLOCK_SIZE == 1 and player.trivial_attempts_1 < C.MAX_ATTEMPTS and player.trivial_attempts_2 < C.MAX_ATTEMPTS

    form_model = 'player'
    form_fields = ['trivial_question_2']

    def error_message(player, value):
        if value['trivial_question_2'] != C.TRIVIAL_ANSWER2:
            player.trivial_attempts_2 = player.trivial_attempts_2 + 1
            left = C.MAX_ATTEMPTS - player.trivial_attempts_2

            if player.trivial_attempts_2 >= C.MAX_ATTEMPTS:
                player.return_study=True

            if player.trivial_attempts_2 < C.MAX_ATTEMPTS:
                result = 'Wrong Answer. Please Try Again. You have ' + str(left)+ ' attempts left.'
                return result
            else:
                result = 'Wrong Answer. The correct Answer is  ' + str(C.TRIVIAL_ANSWER2)+ '. Please input it to proceed.'
                return result


class Complex_Question1(Page):
    template_name = '_static/templates/Complex_Question1.html'
    def is_displayed(player):
        return player.treatment_index==2 and player.subsession.round_number % C.BLOCK_SIZE == 1 and player.complex_attempts_1 < C.MAX_ATTEMPTS

    form_model = 'player'
    form_fields = ['complex_question_1']

    def error_message(player, value):
        if value['complex_question_1'] != C.COMPLEX_ANSWER1:
            player.complex_attempts_1 = player.complex_attempts_1 + 1
            left = C.MAX_ATTEMPTS - player.complex_attempts_1
            
            if player.complex_attempts_1 >= C.MAX_ATTEMPTS:
                player.return_study=True

            if player.complex_attempts_1 < C.MAX_ATTEMPTS:
                result = 'Wrong Answer. Please Try Again. You have ' + str(left)+ ' attempts left.'
                return result
            else:
                result = 'Wrong Answer. The correct Answer is  14. Please input it to proceed.'
                return result


class Complex_Question2(Page):
    template_name = '_static/templates/Complex_Question2.html'
    def is_displayed(player):
        return player.treatment_index==2 and player.subsession.round_number % C.BLOCK_SIZE == 1 and player.complex_attempts_1 < C.MAX_ATTEMPTS and player.complex_attempts_2 < C.MAX_ATTEMPTS

    form_model = 'player'
    form_fields = ['complex_question_2']

    def error_message(player, value):
        if value['complex_question_2'] != C.COMPLEX_ANSWER2:
            player.complex_attempts_2 = player.complex_attempts_2 + 1
            left = C.MAX_ATTEMPTS - player.complex_attempts_2

            if player.complex_attempts_2 >= C.MAX_ATTEMPTS:
                player.return_study=True

            if player.complex_attempts_2 < C.MAX_ATTEMPTS:
                result = 'Wrong Answer. Please Try Again. You have ' + str(left)+ ' attempts left.'
                return result
            else:
                result = 'Wrong Answer. The correct Answer is 4. Please input it to proceed.'
                return result



class Simple_Question1(Page):
    template_name = '_static/templates/Simple_Question1.html'
    def is_displayed(player):
        return player.treatment_index==1 and player.subsession.round_number % C.BLOCK_SIZE == 1 and player.simple_attempts_1 < C.MAX_ATTEMPTS

    form_model = 'player'
    form_fields = ['simple_question_1']

    def error_message(player, value):
        if value['simple_question_1'] != C.SIMPLE_ANSWER1:
            player.simple_attempts_1 = player.simple_attempts_1 + 1
            left = C.MAX_ATTEMPTS - player.simple_attempts_1
            
            if player.simple_attempts_1 >= C.MAX_ATTEMPTS:
                player.return_study=True

            if player.simple_attempts_1 < C.MAX_ATTEMPTS:
                result = 'Wrong Answer. Please Try Again. You have ' + str(left)+ ' attempts left.'
                return result
            else:
                result = 'Wrong Answer. The correct Answer is  ' + str(C.SIMPLE_ANSWER1)+ '. Please input it to proceed.'
                return result


class Simple_Question2(Page):
    template_name = '_static/templates/Simple_Question2.html'
    def is_displayed(player):
        return player.treatment_index==1 and player.subsession.round_number % C.BLOCK_SIZE == 1 and player.simple_attempts_1 < C.MAX_ATTEMPTS and player.simple_attempts_2 < C.MAX_ATTEMPTS

    form_model = 'player'
    form_fields = ['simple_question_2']

    def error_message(player, value):
        if value['simple_question_2'] != C.SIMPLE_ANSWER2:
            player.simple_attempts_2 = player.simple_attempts_2 + 1
            left = C.MAX_ATTEMPTS - player.simple_attempts_2

            if player.simple_attempts_2 >= C.MAX_ATTEMPTS:
                player.return_study=True

            if player.simple_attempts_2 < C.MAX_ATTEMPTS:
                result = 'Wrong Answer. Please Try Again. You have ' + str(left)+ ' attempts left.'
                return result
            else:
                result = 'Wrong Answer. The correct Answer is  ' + str(C.SIMPLE_ANSWER2)+ '. Please input it to proceed.'
                return result
#----------------------------------------------------------------


#----------------------------------------------------------------
# OUTCOMES AND PROLIFIC
#----------------------------------------------------------------
class Results(Page):
    def is_displayed(player):
        return player.subsession.round_number == C.NUM_ROUNDS
    template_name = '_static/templates/Delegation_Results.html'

    @staticmethod
    def vars_for_template(player):
        p = player.in_round(player.payment_round)
        return dict(
            first_payment_round = player.payment_round,
            second_payment_round = player.payment_block*5 + 5,
            payment_block = player.payment_block + 1,
            paricipation_fee = (C.PARTICIPATION_FEE),
            treatment_index = p.treatment_index
            )

class ProlificID(Page):
    form_model = 'player'
    form_fields = ['ProlificID']
    template_name = '_static/templates/ProlificID.html'
    def is_displayed(player):
        return player.subsession.round_number == C.NUM_ROUNDS

    def before_next_page(player, timeout_happened):
        if player.subsession.round_number == C.NUM_ROUNDS:
            set_payoffs(player)
        p = player.in_round(player.subsession.round_number-1)
        if p.trivial_delegation>=-1:
            player.trivial_delegation=p.trivial_delegation
        if p.simple_delegation>=-1:
            player.simple_delegation = p.simple_delegation
        if p.complex_delegation>=-1:
            player.complex_delegation = p.complex_delegation


class ReturnStudy(Page):
    template_name = '_static/templates/ReturnStudy.html'

    def is_displayed(player):
        return player.return_study==True



class Big5(Page):
    def is_displayed(player):
        return player.subsession.round_number == C.NUM_ROUNDS
    template_name = '_static/templates/Big5_Questions.html'

    form_model = 'player'
    form_fields = ['big5_reserved','big5_trusting','big5_lazy','big5_relaxed','big5_artistic','big5_outgoing','big5_blameshifting','big5_job','big5_nervuous','big5_imagination']

class Risk(Page):
    def is_displayed(player):
        return player.subsession.round_number == C.NUM_ROUNDS
    template_name = '_static/templates/Risk_Questions.html'

    form_model = 'player'
    form_fields = ['risk_general','risk_financial','risk_investment','risk_responsibility','wtp_delegation']

#----------------------------------------------------------------
# Delegation Screens
#----------------------------------------------------------------
class DelegationInstructions(Page):
    def is_displayed(player):
        return player.subsession.round_number % C.BLOCK_SIZE == 0
    template_name='_static/templates/DelegationInstructions.html'


class TrivialDelegation(Page):
    def is_displayed(player):
        return player.treatment_index == 0 and player.subsession.round_number % C.BLOCK_SIZE == 0

    template_name='_static/templates/TrivialDelegationDecision.html'
    form_model = 'player'
    form_fields = ['trivial_delegation']
    @staticmethod
    def vars_for_template(player):
        investors = ['A','B','C','D','E']
        expert_indices = [player.expert_index_1, player.expert_index_2, player.expert_index_3, player.expert_index_4, player.expert_index_5]
        experts = [[0 for i in range(0,5)] for i in range(0,5)]
        for i in range(0,5):
            experts[i] = [C.E_PAYMENTS[expert_indices[i]], C.E_RISK[expert_indices[i]], C.E_QUALITY[expert_indices[i]], expert_indices[i], investors[i]]

        return dict(
            experts = [experts[i] for i in range(0,5)],
            )

    @staticmethod
    def before_next_page(player, timeout_happened):
        p = player.in_round(player.subsession.round_number-1)
        if p.simple_delegation>=-1:
            player.simple_delegation = p.simple_delegation
        if p.complex_delegation>=-1:
            player.complex_delegation = p.complex_delegation
        players = player.in_all_rounds()
        for p in players:
            p.trivial_delegation = player.trivial_delegation
        if player.trivial_delegation>=0:
            budget_index = player.budget_index
            expert_number = player.trivial_delegation
            player.trivial_lottery_choice = C.E_TRIVIAL_CHOICES[expert_number][budget_index]
            # making sure the decisions are passed down
            

    #----------------------------------------------------------------


class SimpleDelegation(Page):
    def is_displayed(player):
        return player.treatment_index == 1 and player.subsession.round_number % C.BLOCK_SIZE == 0

    template_name='_static/templates/SimpleDelegationDecision.html'
    form_model = 'player'
    form_fields = ['simple_delegation']
    @staticmethod
    def vars_for_template(player):
        investors = ['A','B','C','D','E']
        expert_indices = [player.expert_index_1, player.expert_index_2, player.expert_index_3, player.expert_index_4, player.expert_index_5]
        experts = [[0 for i in range(0,5)] for i in range(0,5)]
        for i in range(0,5):
            experts[i] = [C.E_PAYMENTS[expert_indices[i]], C.E_RISK[expert_indices[i]], C.E_QUALITY[expert_indices[i]], expert_indices[i], investors[i]]

        return dict(
            experts = [experts[i] for i in range(0,5)],
            )

    @staticmethod
    def before_next_page(player, timeout_happened):
        p = player.in_round(player.subsession.round_number-1)
        if p.trivial_delegation>=-1:
            player.trivial_delegation=p.trivial_delegation
        if p.complex_delegation>=-1:
            player.complex_delegation = p.complex_delegation
        players = player.in_all_rounds()
        for p in players:
            p.simple_delegation = player.simple_delegation
        if player.simple_delegation>=0:
            budget_index = player.budget_index
            expert_number = player.simple_delegation
            player.simple_lottery_choice = C.E_SIMPLE_CHOICES[expert_number][budget_index]
            # making sure the decisions are passed down
            
    #----------------------------------------------------------------

class ComplexDelegation(Page):
    def is_displayed(player):
        return player.treatment_index == 2 and player.subsession.round_number % C.BLOCK_SIZE == 0

    template_name='_static/templates/ComplexDelegationDecision.html'
    form_model = 'player'
    form_fields = ['complex_delegation']
    @staticmethod
    def vars_for_template(player):
        investors = ['A','B','C','D','E']
        expert_indices = [player.expert_index_1, player.expert_index_2, player.expert_index_3, player.expert_index_4, player.expert_index_5]
        experts = [[0 for i in range(0,5)] for i in range(0,5)]
        for i in range(0,5):
            experts[i] = [C.E_PAYMENTS[expert_indices[i]], C.E_RISK[expert_indices[i]], C.E_QUALITY[expert_indices[i]], expert_indices[i], investors[i]]

        return dict(
            experts = [experts[i] for i in range(0,5)],
            )

    @staticmethod
    def before_next_page(player, timeout_happened):
        p = player.in_round(player.subsession.round_number-1)
        if p.trivial_delegation>=-1:
            player.trivial_delegation=p.trivial_delegation
        if p.simple_delegation>=-1:
            player.simple_delegation = p.simple_delegation
        players = player.in_all_rounds()
        for p in players:
            p.complex_delegation = player.complex_delegation
        if player.complex_delegation>=0:
            budget_index = player.budget_index
            expert_number = player.complex_delegation
            # assigning the shares
            player.complex_shares_1 = C.E_COMPLEX_CHOICES[expert_number][0][budget_index]*100
            player.complex_shares_2 = C.E_COMPLEX_CHOICES[expert_number][1][budget_index]*100
            player.complex_shares_3 = C.E_COMPLEX_CHOICES[expert_number][2][budget_index]*100
            player.complex_shares_4 = C.E_COMPLEX_CHOICES[expert_number][3][budget_index]*100
            player.complex_shares_5 = C.E_COMPLEX_CHOICES[expert_number][4][budget_index]*100
            player.complex_shares_6 = C.E_COMPLEX_CHOICES[expert_number][5][budget_index]*100
            # making sure the decisions are passed down
            
    #----------------------------------------------------------------


#------------------------------------------------------------
# PAGE SEQUENCE
#------------------------------------------------------------
page_sequence = [
                DelegationInstructions,
                Trivial_Instructions,
                Trivial_Question1,
                Trivial_Question2,
                ReturnStudy,
                TrivialDelegation,
                Trivial_DecisionScreen,
                Simple_Instructions,
                Simple_Question1,
                Simple_Question2,
                ReturnStudy,
                SimpleDelegation,
                Simple_DecisionScreen,
                Complex_Instructions_P1,
                Complex_Instructions_P2,
                Complex_Instructions_P3,
                Complex_Question1,
                Complex_Question2,
                ReturnStudy,
                ComplexDelegation,
                Complex_DecisionScreen,
                Big5,
                Risk,
                ProlificID,
                Results
                ]
