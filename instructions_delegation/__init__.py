from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'instructions_delegation'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
    
#--------------------------------------------

class DelegationInstructions(Page):
    template_name = '_static/templates/DelegationInstructions.html'
    def is_displayed(player):
        return player.subsession.round_number == C.NUM_ROUNDS


#--------------------------------------------
# PAGE SEQUENCE
#--------------------------------------------


page_sequence = [DelegationInstructions]
