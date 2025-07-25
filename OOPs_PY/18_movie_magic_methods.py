#  Create a class Movie with: 
# ● Attributes: title, rating 
# ● Implement: 
# ○ __str__() → show movie name and rating 
# ○ __eq__() → compare based on rating 
# ○ __lt__() → check if one movie is less rated 
# ○ __add__() → combine rating of two movies 
# ○ __len__() → length of title


class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating

    def __str__(self):
        # Jab print() ya str() call ho, ye chalega
        return f"Movie: {self.title}, Rating: {self.rating}"

    def __eq__(self, other):
        # == operator ke liye, rating compare karega
        if isinstance(other, Movie):
            return self.rating == other.rating
        return False

    def __lt__(self, other):
        # < operator ke liye, rating check karega
        if isinstance(other, Movie):
            return self.rating < other.rating
        return NotImplemented

    def __add__(self, other):
        # + operator ke liye, rating ko add karega
        if isinstance(other, Movie):
            return self.rating + other.rating
        return NotImplemented

    def __len__(self):
        # len() call hone par title ki length dega
        return len(self.title)


m1 = Movie("Inception", 8.8)
m2 = Movie("Interstellar", 8.6)

print(m1)                  # Movie: Inception, Rating: 8.8
print(m2)                  # Movie: Interstellar, Rating: 8.6

print(m1 == m2)            # False (8.8 == 8.6?)
print(m1 < m2)             # False (8.8 < 8.6?)
print(m2 < m1)             # True  (8.6 < 8.8?)

print(m1 + m2)             # 17.4 (sum of ratings)

print(len(m1))             # 9 (length of "Inception")
print(len(m2))             # 12 (length of "Interstellar")
