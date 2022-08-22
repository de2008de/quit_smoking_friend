import time

from os.path import exists


HOLD_BACK_CIGARETTE_FILE = 'hold_back_cigarette.csv'

DATA_FOLDER = 'data/'
FILES = [HOLD_BACK_CIGARETTE_FILE]


class DataManager:
    def __init__(self):
        self.init_files()

    def record_hold_back_cigarette(self):
        current_time = time.time()
        with open(DATA_FOLDER + HOLD_BACK_CIGARETTE_FILE, 'a') as f:
            f.write(str(current_time) + '\n')

    def init_files(self):
        for file in FILES:
            if not exists(DATA_FOLDER + file):
                with open(DATA_FOLDER + file, 'a'):
                    # Create an empty file
                    pass
