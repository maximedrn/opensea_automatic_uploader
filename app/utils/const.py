#!/usr/bin/python
# app/utils/const.py


"""
@author: Maxime Dréan.

Github: https://github.com/maximedrn
Telegram: https://t.me/maximedrn

Copyright © 2022 Maxime Dréan. All rights reserved.
Any distribution, modification or commercial use is strictly prohibited.
"""


# Python internal imports.
from .colors import GREEN, RESET


FIRST_PAGE = (
    f'{GREEN}Created by Maxime Dréan.'
    '\nGithub: https://github.com/maximedrn'
    '\nTelegram: https://t.me/maximedrn'
    '\nEthereum: 0xDD135d5be0a23f6daAAE7D2d0580828c9e09402E'
    '\n\nCopyright © 2022 Maxime Dréan. All rights reserved.'
    '\nAny distribution, modification or commercial use '
    'is strictly prohibited.'
    f'\n\nVersion 1.7.0 - 2022, 28 April.{RESET}'
    '\n\nIf you face any problem, please open an issue.')

ENTER = '\nPRESS [ENTER] TO CONTINUE. '

SECOND_PAGE = (
    f'{GREEN}Created by Maxime Dréan.'
    '\nCopyright © 2022 Maxime Dréan. All rights reserved.'
    '\nAny distribution, modification or commercial use '
    f'is strictly prohibited.{RESET}'
    '\n\nExtension tools available here: https://maximedrn.gumroad.com/'
    '\nTutorials on YouTube: https://www.youtube.com/channel/UCoqpR1OLb'
    'swIyQVatKBoGxA')

PASSWORD = '\nWhat is your wallet password? '

RECOVERY_PHRASE = '\nWhat is your wallet recovery phrase? '

PRIVATE_KEY = '\nWhat is your account private key? ' + \
    '(Press [ENTER] to ignore this step) '

ALL_DONE = (
    f'\n{GREEN}All done!{RESET}'
    '\nIn order to support me, you can make donations at this address:'
    '\n0xDD135d5be0a23f6daAAE7D2d0580828c9e09402E (Ethereum).')