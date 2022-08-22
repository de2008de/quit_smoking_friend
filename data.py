import datetime
import math
import random
import time

from os.path import exists


HOLD_BACK_CIGARETTE_FILE = 'hold_back_cigarette.csv'
FIRST_DAY_QUIT_FILE = 'first_day_quit.txt'

DATA_FOLDER = 'data/'
FILES = [HOLD_BACK_CIGARETTE_FILE, FIRST_DAY_QUIT_FILE]


class DataManager:
    def __init__(self):
        self.init_files()
        self.jokes = self.load_jokes()

    def record_hold_back_cigarette(self):
        current_time = time.time()
        with open(DATA_FOLDER + HOLD_BACK_CIGARETTE_FILE, 'a') as f:
            f.write(str(current_time) + '\n')

    def random_joke(self):
        idx = random.randint(0, len(self.jokes) - 1)
        return self.jokes[idx]

    def get_num_hold_back(self):
        with open(DATA_FOLDER + HOLD_BACK_CIGARETTE_FILE, 'r') as f:
            lines = f.readlines()
        return len(lines)

    def get_days_quit(self):
        with open(DATA_FOLDER + FIRST_DAY_QUIT_FILE, 'r') as f:
            start_time = f.read()
        start_day = datetime.datetime.fromtimestamp(float(start_time))
        now_day = datetime.datetime.utcnow()
        total_seconds = (now_day - start_day).total_seconds()
        return math.trunc(total_seconds / 60 / 60 / 24)

    def load_jokes(self):
        with open('assets/jokes/one_liner_jokes.txt', 'r') as f:
            jokes = f.readlines()
        return jokes

    def init_files(self):
        for file in FILES:
            if not exists(DATA_FOLDER + file):
                with open(DATA_FOLDER + file, 'a') as f:
                    # Create an empty file
                    pass

                if file == FIRST_DAY_QUIT_FILE:
                    with open(DATA_FOLDER + file, 'w') as f:
                        f.write(str(time.time()) + '\n')
