
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

# binary search
def find_cruise_length(cruise_lengths, vacation_length):
    left = 0
    right = len(cruise_lengths) - 1

    while left <= right:
        mid = (left + right) // 2
        if cruise_lengths[mid] > vacation_length:
            right = mid -1
        elif cruise_lengths[mid] < vacation_length:
            left = mid + 1
        else:
            return True

    return False

print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))

print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))

def find_cabin_index(cabins, preferred_deck):
    low = 0
    high = len(cabins) - 1
    def helper(low, high, cabins, preferred_deck):
        if low > high:
            return low
        
        mid = (low + high) // 2
        if cabins[mid] < preferred_deck:
            return helper(mid + 1, high, cabins, preferred_deck)
        elif cabins[mid] > preferred_deck:
            return helper(low, mid - 1, cabins, preferred_deck)
        else:
            return mid
    return helper(low, high, cabins, preferred_deck)
print(find_cabin_index([1, 3, 5, 6], 5))
print(find_cabin_index([1, 3, 5, 6], 2))
print(find_cabin_index([1, 3, 5, 6], 7))