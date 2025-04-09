#score_manager.py
import os

BEST_SCORE_FILE = "best_score.txt"

def load_best_score():
    if not os.path.exists(BEST_SCORE_FILE):
        return None
    with open(BEST_SCORE_FILE, "r") as f:
        return int(f.read())

def save_best_score(score):
    with open(BEST_SCORE_FILE, "w") as f:
        f.write(str(score))