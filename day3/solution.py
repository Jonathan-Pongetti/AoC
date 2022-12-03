import string
from itertools import islice

def puzzle1():

    with open('input.txt') as f:
        lines = f.readlines()

    alphabet = list(string.ascii_letters)
    total = 0

    for line in lines:
        line = line.strip()
        compartment1 = line[:len(line)//2]
        compartment2 = line[len(line)//2:]
        shared = ''.join(set(compartment1).intersection(compartment2))
        total += alphabet.index(shared) + 1

    print(total)

def puzzle2():
    alphabet = list(string.ascii_letters)
    total = 0
    with open('input.txt') as f:
        while True:
            lines = list(islice(f,3))
            if not lines:
                break
            
            shared = set(lines[0].strip()).intersection(set(lines[1].strip())).intersection(set(lines[2].strip()))
            total += alphabet.index(next(iter(shared))) + 1
    

    print(total)
