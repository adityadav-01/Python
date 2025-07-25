#  WAP to ask the user to enter names of their 3 favorite movies & store them in a list.

# Program to input 3 favorite movies and store them in a list

# Step 1: Create empty list
favorite_movies = []

# Step 2: Take 3 movie names from user using loop
for i in range(3):
    movie = input(f"Enter favorite movie {i+1}: ")
    favorite_movies.append(movie)

# Step 3: Print the final list
print("Your favorite movies are:", favorite_movies)