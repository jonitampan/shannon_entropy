import math
import random
def shannon_entropy(sentence):
    entropy = 0
    for character_i in range(256):
        Px = sentence.count(chr(character_i))/len(sentence)
        if Px > 0:
            entropy += - Px * math.log(Px, 2)
    return entropy
print(shannon_entropy("google.com"))
