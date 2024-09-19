# Task 2: Movie Budget Analysis - Python Mini Project

import pandas as pd
import numpy as np

movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

# input new movies
num_movies = int(input("Enter the number of movies you want to add:"))
for movie in range(num_movies):
    new_movies = input("Enter new movie name:")
    new_budget = int(input("Enter new movie Budget:"))
    movies.append((new_movies,new_budget))
 
# creating data frame and Columns
df = pd.DataFrame(movies,columns=["Movie","Budget"])
print(df)

# Calculating Budget
avg_budget = np.mean(df["Budget"])
print("The average of movies:",avg_budget)


# higher budget movies

high_budget = df[df["Budget"] > avg_budget].copy()
high_budget["Above avg"] = high_budget["Budget"] - avg_budget
print("The high budget movies\n",high_budget)


