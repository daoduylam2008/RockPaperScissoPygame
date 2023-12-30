import pandas as pd
import sklearn
import random
import csv


class Computer:

    def __init__(self, choice):
        self.player = choice
        self.computer_choices = ["rock", "paper", "scissors"]
        self.history = []
        self.our_state = []

        with open('data/history.txt', 'r') as file:
            self.history = [int(i) for i in file.read()]
        with open('data/history1.txt', 'r') as file1:
            self.our_state = [int(i) for i in file1.read()]

    def easy(self):
        return random.choice(self.computer_choices)

    def medium(self):
        if not self.our_state or self.our_state == 6: # if draw or haven't play
            return random.choice(self.computer_choices)
        elif self.our_state[-1] == 4: # if computer win
            return self.computer_choices[int(self.history[-1])-2]
        elif self.our_state[-1] == 5: # if computer lose
            if self.history[-1]-1 <= 1:
                return self.computer_choices[self.history[-1]]
            else: return self.computer_choices[0]

    def hard(self):
        fields = ['player_choice', 'our_state']
        rows = []
        for i in range(len(self.history)):
            rows.append([self.history[i], self.our_state[i]])
        with open('data/temp.csv', 'w') as csv_file:
            csvwriter = csv.writer(csv_file)
            csvwriter.writerow(fields)
            csvwriter.writerows(rows)
        df = pd.read_csv('data/temp.csv')
        X = df.iloc[:,0]