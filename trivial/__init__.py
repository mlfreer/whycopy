from otree.api import *


doc = """
Your app description
"""

# models
class C(BaseConstants):
    NAME_IN_URL = 'trivial'
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



    # defining experts:
    EXPERTS_average_payoff = [0 for i in range(0,5)]

    EXPERTS_risk_rating = [0 for i in range(0,5)]

    EXPERTS_quality_rating = [0 for i in range(0,5)]

    EXPERTS_choices = [[0 for i in range(0,5)] for i in range(0,5)]



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # lottery choice:
    lottery_choice = models.IntegerField(min=0,max=1)

    # delegation choice:
    to_delegate = models.IntegerField(min=0,max=1)
    whom_delegate = models.IntegerField(min=0,max=C.NUM_OF_EXPERTS)


# PAGES
class DecisionScreen(Page):
    form_model = 'player'
    form_fields = ['lottery_choice']

    def vars_for_template(player):
        i = player.subsession.round_number-1
        return dict(
            lottery_1 = C.Lottery1[i],
            lottery_2 = C.Lottery2[i],
            )


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [
                DecisionScreen, 
                ResultsWaitPage, 
                Results
                ]



