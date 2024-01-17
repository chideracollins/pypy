
class  Rating:
    def __init__(self, age, score, rating):
        self.age = age
        self.score = score
        self.rating = rating
"""instance = Rating(43, 80, "intelligent")
print(instance.score)"""
dataL = {
    "Amaka": [25, 78, "intelligent"],
    "Emeka": [12, 87, "Genius"],
}
for x, y in dataL.items():
    globals()[x] = Rating(y[0], y[1], y[2])
print(Amaka.score)
print(Emeka.age)
