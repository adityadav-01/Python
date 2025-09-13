reviews = [
    "This product is very good",
    "Worst experience ever",
    "I love this phone",
    "Battery life is bad",
    "Camera quality is excellent",
    "Not worth the money"
]

positive_words = ["good", "excellent", "love", "best", "nice"]

positive_reviews = []

for review in reviews:
    for word in positive_words:
        if word in review.lower():  
            positive_reviews.append(review)
            break  

print("Positive reviews:")
for r in positive_reviews:
    print("-", r)
