import random
import time

from os.path import exists


HOLD_BACK_CIGARETTE_FILE = 'hold_back_cigarette.csv'

DATA_FOLDER = 'data/'
FILES = [HOLD_BACK_CIGARETTE_FILE]


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

    def load_jokes(self):
        with open('assets/jokes/one_liner_jokes.txt', 'r') as f:
            jokes = f.readlines()
        return jokes

    def init_files(self):
        for file in FILES:
            if not exists(DATA_FOLDER + file):
                with open(DATA_FOLDER + file, 'a'):
                    # Create an empty file
                    pass
