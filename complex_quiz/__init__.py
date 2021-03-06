from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'complex_quiz'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    MAX_ATTEMPTS = 3

    ANSWER1 = 3
    ANSWER2 = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    attempts1 = models.IntegerField(min=0, max=10, initial=0)
    attempts2 = models.IntegerField(min=0, max=10, initial=0)

    question1 = models.IntegerField(min=1,max=4)
    question2 = models.IntegerField(min=1,max=4)


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
                result = 'Wrong Answer. The correct Answer is  10*20 + 10*40 + 20*40 = 1400. Please input it to proceed.'
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
                result = 'Wrong Answer. The correct Answer is  (50*40 + 100*60)/1000 = 8. Please input it to proceed.'
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
