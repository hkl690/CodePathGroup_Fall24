from itertools import count


def count_suits_iterative(suits):
    count = 0

    for suit in suits:
        count += 1
    return count

# def count_suits_recursive(suits):

#     if not suits:
#         return 0
#     return 1 + count_suits_recursive(suits[1:])

# print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
# print(count_suits_recursive(["Mark I", "Mark I", "Mark III", "Mark IV"]))

def count_suits_recursive(suits):

    if not suits:
        return 0
    first = suits[0]
    remaining_uniques = count_suits_recursive(suits[1:])

    if first in suits[1:]:
        return remaining_uniques
    else:
        return 1 + remaining_uniques

print(count_suits_recursive(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))


# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1

def fibonacci_growth(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_growth(n-1) + fibonacci_growth(n-2)



print(fibonacci_growth(5))
print(fibonacci_growth(8))


def count_deposits(resources):
    if not resources:
        return 0

    if resources[0] == 'V':
        return 1 + count_deposits(resources[1:])
    else:
        return count_deposits(resources[1:])

print(count_deposits("VVVVV"))
print(count_deposits("VXVYGA"))