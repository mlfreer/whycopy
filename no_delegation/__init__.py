from otree.api import *


doc = """
Your app description
"""


# CONSTANTS
class C(BaseConstants):
    NAME_IN_URL = 'no_delegation'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1



# CLASSES
class Subsession(BaseSubsession):
    NUM_ROUNDS = 1
    NUM_ROUNDS = 15

    # Probability of HEADS:
    P_HEADS = .5

    # Tokens budget:
    EXCHANGE_RATE = 20

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


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # complex treatments variables:
    # decision variables
    complex_shares_1 = models.FloatField()
    complex_shares_2 = models.FloatField()
    complex_shares_3 = models.FloatField()
    complex_shares_4 = models.FloatField()
    complex_shares_5 = models.FloatField()
    tokens = models.FloatField()
    # budget index:
    complex_budget_index = models.IntegerField(min=0,max=4)
    complex_final_budget_index = models.IntegerField(min=0,max=4)
    # state of the world
    complex_state_of_the_world = models.BooleanField(initial=False)



    # simple treatment variables
    # choice variables
    simple_lottery_choice =  models.IntegerField(min=1,max=6)
    # budget index
    simple_budget_index = models.IntegerField(min=0,max=4)
    simple_final_budget_index = models.IntegerField(min=0,max=4)
    # state of the world
    simple_state_of_the_world = models.BooleanField(initial=False)


    # trivial treatment variables
    # choice variables
    trivial_lottery_choice =  models.IntegerField(min=1,max=6)
    # budget index
    trivial_budget_index = models.IntegerField(min=0,max=4)
    trivial_final_budget_index = models.IntegerField(min=0,max=4)
    # state of the world
    trivial_state_of_the_world = models.BooleanField(initial=False)







# PAGES
class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
