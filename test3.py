import numpy as np
import random


class Computer:

    def __init__(self, choice):
        self.player = choice
        self.computer_choices = ["rock", "paper", "scissors"]
        with open("data/history.txt") as file:
            self.history = [i for i in str(file.read())]

    def easy(self):
        # Return a random choice
        return random.choice(self.computer_choices)

    def hard(self):
        # Count the occurrences of each choice in the history
        choice_counts = np.bincount(self.history)

        # If there is no history, predict randomly
        if len(choice_counts) == 0:
            return np.random.choice(self.computer_choices)

        # Determine the most frequent move
        most_frequent_move = np.argmax(choice_counts)

        # Map the most frequent move to its corresponding label
        if most_frequent_move == 0:
            predicted_move = "rock"
        elif most_frequent_move == 1:
            predicted_move = "paper"
        else:
            predicted_move = "scissors"
        return predicted_move
