# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 01:41:12 2024

@author: TOSHIBA
"""

#%%
class average_budget:
    def __init__(self, movies):
          self.movies = movies

    # adding new movies
    def new_movies(self):
        num_movies = int(input("Enter number of movies you want to add: "))
        for movie in range(num_movies):
            new_movies = input("Enter new movie name: ")
            new_budget = int(input("Enter new movie budget: "))
            self.movies.append((new_movies, new_budget))

    # average of budget        
    def average_budget(self):
        total_budget = sum(Budget for movie, Budget in self.movies)
        avg_budget = total_budget / len(self.movies)
        print("The average of all movies:", avg_budget)
        return avg_budget

    # high budget    
    def high_budget(self, avg_budget):
        for name, budget in self.movies:
            if budget > avg_budget:
                print(f"{name} has a budget of {budget}\n which is above the average.")

    # display method
    def display(self):
        self.new_movies()
        avg_budget = self.average_budget()
        self.high_budget(avg_budget)

movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

o = average_budget(movies)
o.display()