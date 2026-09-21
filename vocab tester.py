import random
import statistics
import math
from vocabset1 import nouns, verbs, adjectives, unchangeable

total = len(nouns) + len(adjectives) + len(unchangeable) + len(verbs)

correct = 0
wrong = 0

answer = ""

answered = [0 for i in range(total)]
incorrect = set()
incorrectperm = set()

def getkey(n):
    if n < len(nouns):
        return list(nouns.keys())[n]
    elif n < len(nouns) + len(verbs):
        return list(verbs.keys())[n-len(nouns)]
    elif n < len(nouns) + len(verbs) + len(adjectives):
        return list(adjectives.keys())[n-len(nouns)-len(verbs)]
    else:
        return list(unchangeable.keys())[n-len(nouns)-len(verbs)-len(adjectives)]

def getdef(n):
    key = getkey(n)
    type = []
    if n < len(nouns): type = nouns
    elif n < len(nouns) + len(verbs): type = verbs
    elif n < len(nouns) + len(verbs) + len(adjectives): type = adjectives
    else: type = unchangeable
    return type[key].lower()

while not answer == "end":
    q = random.randint(0, total - 1)
    while answered[q] > math.floor(statistics.mean(answered)) and not q in incorrect:
        q = random.randint(0, total - 1)
    type = []
    key = getkey(q)
    print("")
    #print("Type 'end' to finish.")
    if q < len(nouns): 
        print(f"{correct + wrong + 1}. Enter the nominative singular.")
    elif q < len(nouns) + len(verbs): 
        print(f"{correct + wrong + 1}. Enter the 1st person singular present active.")
    elif q < len(nouns) + len(verbs) + len(adjectives): 
        print(f"{correct + wrong + 1}. Enter the nominative singular male.")
    else: 
        print(f"{correct + wrong + 1}. Enter the Latin translation.")
    print(key)
    answer = input("Your answer: ")
    if answer == 'end':
        break
    if answer.lower() == getdef(q).lower():
        correct += 1
        print("Correct.")
        incorrect.discard(q)
        
    else:
        wrong += 1
        print(f"Incorrect. The correct answer was {getdef(q)}.")
        incorrect.add(q)
        incorrectperm.add(q)
    answered[q] += 1

print("")
print("Congratulations! Here are your stats:")
print(f"Correct: {correct}/{correct + wrong}")
print(f"Incorrect: {wrong}/{correct + wrong}")
try: print(f"Accuracy: {round(100 * correct/(correct + wrong),2)}%")
except: print("Accuracy unavailable.")
print("")
print("Here are your incorrectly answered vocab words:")
for n in incorrectperm:
    print(f"{getdef(n)+':':<{15}}{getkey(n)}")



