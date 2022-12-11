from os import environ

SESSION_CONFIGS = [
     dict(
         name='Trivial_Instructions',
         app_sequence=['consent_form','instructions_trivial'],
         num_demo_participants=1,
     ),
     dict(
         name='Simple_Instructions',
         app_sequence=['consent_form','simple_instructions'],
         num_demo_participants=1,
     ),
     dict(
         name='Complex_Instructions',
         app_sequence=['consent_form','instructions_complex'],
         num_demo_participants=1,
     ),
     dict(
         name='Instructions_Delegation',
         app_sequence=['instructions_delegation'],
         num_demo_participants=1,
     ),
     dict(
         name='Trivial_Quiz',
         app_sequence=['trivial_quizz'],
         num_demo_participants=1,
     ),
     dict(
         name='Simple_Quiz',
         app_sequence=['simple_quiz'],
         num_demo_participants=1,
     ),
     dict(
         name='Complex_Quiz',
         app_sequence=['complex_quiz'],
         num_demo_participants=1,
     ),
     dict(
         name='No_Delegation_Online',
         app_sequence=['consent_form','no_delegation'],
         num_demo_participants=1,
     ),
     dict(
         name='Delegation_Online',
         app_sequence=['consent_form','delegation'],
         num_demo_participants=1,
     ),
     dict(
         name='Delegation_No_Info_Online',
         app_sequence=['consent_form','delegation_no_info'],
         num_demo_participants=1,
     ),
     dict(
         name='Delegation_No_Jars_Online',
         app_sequence=['consent_form','delegation_no_jars'],
         num_demo_participants=1,
     ),

]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=.1, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

DEBUG=False
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
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '1668786856812'


