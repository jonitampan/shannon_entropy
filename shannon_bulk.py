import math
import random
import csv

def shannon_entropy(sentence):
    entropy = 0
    for character_i in range(256):
        Px = sentence.count(chr(character_i))/len(sentence)
        if Px > 0:
            entropy += - Px * math.log(Px, 2)
    return entropy
#print(shannon_entropy("google.com"))
  

with open(r"C:\Users\IEUser\Downloads\top-head.csv","r") as f:
    data = csv.reader(f)
    for row in data:
        score = (shannon_entropy(str(row)))        
        if score > 4.7:
            print("[+] Domain : %s Score : %s "% (row[0],score) )        