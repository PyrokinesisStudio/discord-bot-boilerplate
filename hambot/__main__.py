import os
import sys
import argparse
from bot.bot import HamBot

if __name__ == '__main__':

    bot = HamBot()

    # check for configuration file that holds user bot ID and Token
    if not os.path.exists('{0}\{1}'.format(os.getcwd(), 'config.ini')):
        print('Creating base configuration file...')
        bot.create_config()
    else:
        bot.get_token()

    bot.run()
