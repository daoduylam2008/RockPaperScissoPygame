import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.model_selection import train_test_split
import random
import csv
import time


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
        if not self.our_state or self.our_state == 6:
            return random.choice(self.computer_choices)
        elif self.our_state[-1] == 4:
            return self.computer_choices[int(self.history[-1]) - 2]
        elif self.our_state[-1] == 5:
            if self.history[-1] - 1 <= 1:
                return self.computer_choices[self.history[-1]]
            else:
                return self.computer_choices[0]

    def hard(self):
        player_choice_dict = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
        our_state_dict = {4: 'Win', 5: 'Lose', 6: 'Draw'}
        fields = ['player_choice', 'our_choice', 'our_state']
        rows = []
        our_choice = ''
        for i in range(len(self.history) - 1):
            if our_state_dict[self.our_state[i]] == 'Draw':
                our_choice = player_choice_dict[self.history[i]]
            elif our_state_dict[self.our_state[i]] == 'Win':
                match player_choice_dict[self.history[i]]:
                    case 'Rock':
                        our_choice = 'Paper'
                    case 'Paper':
                        our_choice = 'Scissors'
                    case 'Scissors':
                        our_choice = 'Rock'
            else:
                match player_choice_dict[self.history[i]]:
                    case 'Rock':
                        our_choice = 'Scissors'
                    case 'Paper':
                        our_choice = 'Rock'
                    case 'Scissors':
                        our_choice = 'Paper'
            rows.append([player_choice_dict[self.history[i]], our_choice, our_state_dict[self.our_state[i]]])
        rows.append([player_choice_dict[self.history[len(self.history) - 1]], None, 'Win'])
        with open('data/temp.csv', 'w') as csv_file:
            csvwriter = csv.writer(csv_file)
            csvwriter.writerow(fields)
            csvwriter.writerows(rows)
        df = pd.read_csv('data/temp.csv')
        X = df.iloc[:, :2].values
        y = df.iloc[:, 2].values
        ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0, 1])], remainder='passthrough')
        X = ct.fit_transform(X)
        le = LabelEncoder()
        y = le.fit_transform(y)
        imputer = SimpleImputer(missing_values=np.nan, strategy="mean")


start = time.time()
a = Computer('rock').hard()
print(a)
print(time.time() - start)
