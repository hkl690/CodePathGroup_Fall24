#   live share link:
#   https://prod.liveshare.vsengsaas.visualstudio.com/join?45216BC74E998E42D1DDBCA7D4B6AED5E9A3 

from collections import Counter


def unique_souvenir_counts(souvenirs):
    counts = Counter(souvenirs)
    print(counts)
    countsSet = set(counts.values())
    print(countsSet)
    return len(counts) == len(countsSet)


souvenirs = ["keychain", "hat", "hat", "keychain", "keychain", "postcard"] # True
print(unique_souvenir_counts(souvenirs))

souvenirs = ["postcard", "postcard", "postcard", "postcard"] # True
print(unique_souvenir_counts(souvenirs))

souvenirs = ["keychain", "magnet", "hat", "candy", "postcard", "stuffed bear"] # False
print(unique_souvenir_counts(souvenirs))

print("hello")

