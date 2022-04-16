from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'complex_quiz'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    MAX_ATTEMPTS = 3

    ANSWER1 = 1400
    ANSWER2 = 4


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    attempts1 = models.IntegerField(min=0, max=10, initial=0)
    attempts2 = models.IntegerField(min=0, max=10, initial=0)

    question1 = models.IntegerField(min=0,max=10000)
    question2 = models.IntegerField(min=0,max=10000)


# PAGES
class Welcome(Page):
    template_name = '_static/templates/Welcome.html'

class Question1(Page):
    def is_displayed(player):
        return player.attempts1 < C.MAX_ATTEMPTS

    form_model = 'player'
    form_fields = ['question1']

    def error_message(player, value):
        if value['question1'] != C.ANSWER1:
            player.attempts1 = player.attempts1 + 1
            left = C.MAX_ATTEMPTS - player.attempts1
            
            if player.attempts1 < C.MAX_ATTEMPTS:
                result = 'Wrong Answer. Please Try Again. You have ' + str(left)+ ' attempts left.'
                return result
            else:
                result = 'Wrong Answer. The correct Answer is  ' + str(C.ANSWER1)+ '. Please input it to proceed.'
                return result


class Question2(Page):
    def is_displayed(player):
        return player.attempts1 < C.MAX_ATTEMPTS and player.attempts2 < C.MAX_ATTEMPTS

    form_model = 'player'
    form_fields = ['question2']

    def error_message(player, value):
        if value['question2'] != C.ANSWER2:
            player.attempts2 = player.attempts2 + 1
            left = C.MAX_ATTEMPTS - player.attempts2
            if player.attempts2 < C.MAX_ATTEMPTS:
                result = 'Wrong Answer. Please Try Again. You have ' + str(left)+ ' attempts left.'
                return result
            else:
                result = 'Wrong Answer. The correct Answer is  ' + str(C.ANSWER2)+ '. Please input it to proceed.'
                return result


class ReturnStudy(Page):
    template_name = '_static/templates/ReturnStudy.html'

    def is_displayed(player):
        return player.attempts1 >= C.MAX_ATTEMPTS or player.attempts2 >= C.MAX_ATTEMPTS


page_sequence = [
            Welcome,
            Question1,
            Question2,
            ReturnStudy
]
