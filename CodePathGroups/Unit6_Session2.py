# Given an array of integers, write a function to return the indices of the two numbers that add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Understand: arr of ints, target value, return 2 indexes gets us sum of target value
# clarifying: no values? return [-1,-1], at least two? no, can get 1 or 0
# Match: Two pointer-need to sort

def twoSum(nums, target):
    hashMap = dict()
    # x + y = target
    # target - y == x

    for i, num in enumerate(nums):
        diff = target - num
        if diff in hashMap:
            return [hashMap[diff], i]

        hashMap[num] = i

    return [-1, -1]

# def twoSum(nums, target):
#     left = 0
#     right = len(nums) -1

#     if len(nums) <= 1:
#         return [-1, -1]

#     while left < right:
#         if nums[left] + nums[right] == target:
#             return [left, right]
#         elif nums[left] + nums[right] < target:
#             left += 1
#         else:
#             right -= 1
#     return [-1, -1]

nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))

# Problem 1: Wild Goose Chase
# You're a detective and have been given an anonymous tip on your latest case, but something about it seems fishy - you suspect the clue might be a red herring meant to send you around in circles. Write a function is_circular() that accepts the head of a singly linked list clues and returns True if the tail of the linked list points at the head of the linked list. Otherwise, return False.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_circular(clues):
    if not clues:
        return False

    current = clues

    while current.next:
        if current.next == clues:
            return True
        current = current.next

    return False



clue1 = Node("The stolen goods are at an abandoned warehouse")
clue2 = Node("The mayor is accepting bribes")
clue3 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue1

print(is_circular(clue1))

# Problem 2: Breaking the Cycle
# All the clues that lead us in circles are false evidence we need to purge! Given the head of a linked list evidence, clean up the evidence list by identifying any false clues. Write a function collect_false_evidence() that returns an array containing all values that are part of any cycle in evidence. Return the values in any order.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def collect_false_evidence(evidence):
    if not evidence:
        return []

    slow = evidence
    fast = evidence
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        # if there is a cycle
        if fast == slow:
            break

    # if no cycle return []
    if fast != slow:
        return []

    results = []
    fast = fast.next
    while fast != slow:
        results.append(fast.value)
        fast = fast.next
    results.append(fast.value)
    return results

clue1 = Node("Unmarked sedan seen near the crime scene")
clue2 = Node("The stolen goods are at an abandoned warehouse")
clue3 = Node("The mayor is accepting bribes")
clue4 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue4
clue4.next = clue2

clue5 = Node("A masked figure was seen fleeing the scene")
clue6 = Node("Footprints lead to the nearby woods")
clue7 = Node("A broken window was found at the back")
clue5.next = clue6
clue6.next = clue7

print(collect_false_evidence(clue1))
print(collect_false_evidence(clue5))

# Problem 3: Prioritizing Suspects
# You've identified a list of suspect, but time is limited and you won't be able to question all of them today. Write a function partition() to help prioritize the order in which you question suspects. Given the head of a linked list of integers suspect_ratings, where each integer represents the suspiciousness of the a given suspect and a value threshold, partition the linked list such that all nodes with values greater than threshold come before nodes with values less than or equal to threshold.

# Return the head of the partitioned list.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def partition(suspect_ratings, threshold):
    if not suspect_ratings:
        return None
    
    greater_head = Node(0)  # Temporary head for greater-than-threshold list
    less_or_equal_head = Node(0)  # Temporary head for less-or-equal list
    
    greater = greater_head
    less_or_equal = less_or_equal_head
    
    current = suspect_ratings
    while current:
        if current.value > threshold:
            greater.next = current
            greater = greater.next
        else:
            less_or_equal.next = current
            less_or_equal = less_or_equal.next
        current = current.next
    
    # Combine the two lists
    greater.next = less_or_equal_head.next
    less_or_equal.next = None  # Ensure the last node points to None
    
    # Check if the greater list is empty
    if greater_head.next:
        return greater_head.next
    else:
        return less_or_equal_head.next

suspect_ratings = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))

print_linked_list(partition(suspect_ratings, 3))