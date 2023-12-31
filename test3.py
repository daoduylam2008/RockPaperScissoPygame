import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
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
        if len(self.history) <= 2:
            return random.choice(self.computer_choices)
        else:
            player_choice_dict = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
            our_state_dict = {4: 'Win', 5: 'Lose', 6: 'Draw'}
            fields = ['player_choice', 'our_choice', 'our_state']
            rows = []
            our_choice = 0
            for i in range(len(self.history) - 1):
                if our_state_dict[self.our_state[i]] == 'Draw':
                    our_choice = self.history[i]
                elif our_state_dict[self.our_state[i]] == 'Win':
                    match player_choice_dict[self.history[i]]:
                        case 'Rock':
                            our_choice = 2
                        case 'Paper':
                            our_choice = 3
                        case 'Scissors':
                            our_choice = 1
                else:
                    match player_choice_dict[self.history[i]]:
                        case 'Rock':
                            our_choice = 3
                        case 'Paper':
                            our_choice = 1
                        case 'Scissors':
                            our_choice = 2
                rows.append([self.history[i], our_choice, self.our_state[i]])

            with open('data/temp.csv', 'w') as csv_file:
                csvwriter = csv.writer(csv_file)
                csvwriter.writerow(fields)
                csvwriter.writerows(rows)

            df = pd.read_csv('data/temp.csv')
            features = ['player_choice', 'our_state']
            X = df.dropna(axis=0)[features].values
            y = df.dropna(axis=0)['our_choice']
            X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=0)

            dt_model = DecisionTreeClassifier(random_state=1)
            dt_model.fit(X_train, y_train)
            dt_model_score = dt_model.score(X_test, y_test)

            rf_model = RandomForestClassifier(random_state=1)
            rf_model.fit(X_train, y_train)
            rf_model_score = rf_model.score(X_test, y_test)

            if rf_model_score >= dt_model_score:
                return player_choice_dict[(rf_model.predict([[self.history[len(self.history) - 1], 4]])[0])]
            else:
                return player_choice_dict[(dt_model.predict([[self.history[len(self.history) - 1], 4]])[0])]
