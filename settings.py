from os import environ

SESSION_CONFIGS = [
#     dict(
#         name='No_Delegation_Online',
#         app_sequence=['consent_form','no_delegation'],
#         num_demo_participants=1,
#     ),
#     dict(
#         name='Delegation_Online',
#         app_sequence=['consent_form','delegation'],
#         num_demo_participants=1,
#     ),
#     dict(
#         name='Delegation_No_Info_Online',
#         app_sequence=['consent_form','delegation_no_info'],
#         num_demo_participants=1,
#     ),
#     dict(
#         name='Delegation_No_Quality_Online',
#         app_sequence=['consent_form','delegation_no_quality'],
#         num_demo_participants=1,
#     ),
#     dict(
#         name='Delegation_WTP',
#         app_sequence=['consent_form','delegation_wtp'],
#         num_demo_participants=1,
#     ),
#     dict(
#         name='Delegation_WTP_with_investors_list',
#         app_sequence=['consent_form','delegation_wtp_investors_list'],
#         num_demo_participants=1,
#     ),
#     dict(
#         name="Delegation_Two_Stage",
#         app_sequence=['consent_form','delegation_salient_price'],
#         num_demo_participants=1,
#     ),
     dict(
         name="Delegation_After_Quality_Info",
         app_sequence=['consent_form','Delegation_After_Quality'],
         num_demo_participants=1,
         #completionlink="https://app.prolific.co/submissions/complete?cc=6E1B1776",
     ),
     dict(
         name="Delegation_Before_Quality_Info",
         app_sequence=['consent_form','Delegation_Before_Quality'],
         num_demo_participants=1,
         #completionlink="https://app.prolific.co/submissions/complete?cc=6E1B1776",
     ),

]
# DEBUG MODE:
DEBUG=False


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=.1, 
    participation_fee=0.00, 
    doc="",
    #completionlink="https://app.prolific.co/submissions/complete?cc=6E1B1776",
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'GBP'
USE_POINTS = False

ROOMS = [
    dict(
        name='econ_lab',
        display_name='Economics Lab',
        participant_label_file='_rooms/econ_lab.txt',
        use_secure_urls=False
    ),
    dict(
        name='your_prolific_study',
        display_name='your_prolific_study',
        # participant_label_file='_rooms/your_study.txt',
        # use_secure_urls=True,
    ),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '1668786856812'


