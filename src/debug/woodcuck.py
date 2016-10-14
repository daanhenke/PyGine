import os
import datetime

import sys


class WoodChuck(object):
    def __init__(self, pygine, to_file, to_console, mirror_console_emulator, log_path):
        self.engine = pygine

        self.to_file = to_file
        self.to_console = to_console
        self.mirror_console_emulator = mirror_console_emulator

        if to_file:
            self.creation_date = '{:%Y%m%d%H%M%S}'.format(datetime.datetime.now())
            self.log_file_name = self.creation_date + '.logdump'
            if os.path.isfile(os.path.join('logs', self.creation_date + '.logdump')):
                sys.exit(5001)
            else:
                self.log_file_name = self.creation_date
                print __file__
                self.log_file = open(os.path.join(self.log_path, ), 'w')
        return

    def log_raw(self, text, message_type, colour):

        return