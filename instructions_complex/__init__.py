from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'instructions_complex'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class InstructionsPage1(Page):
    pass

class InstructionsPage2(Page):
    pass

class InstructionsPage3(Page):
    pass
    
page_sequence = [
            InstructionsPage1,
            InstructionsPage2,
            InstructionsPage3,
    ]
