def getStartingPositions():
    start = [[]] * 9 
    with open('./day5/starting.txt') as f:
        lines = f.readlines()

    for idx, line in enumerate(lines):
        line = line.strip().split(',')
        start[idx] = line    

    return start

def puzzle1():
    starting = getStartingPositions()

    with open('./day5/newinput.txt') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip().split(' ')
        amtmov = int(line[1])
        fromstack = int(line[3])-1
        tostack = int(line[5])-1
        for box in range(amtmov):
            starting[tostack].append(starting[fromstack].pop())

    
    for stack in starting:
        print(stack.pop())




def puzzle2():
    starting = getStartingPositions()

    with open('./day5/newinput.txt') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip().split(' ')
        amtmov = int(line[1])
        fromstack = int(line[3])-1
        tostack = int(line[5])-1

        remove = starting[fromstack][len(starting[fromstack])-amtmov:]
        del starting[fromstack][len(starting[fromstack])-amtmov:]
        for box in remove:
            starting[tostack].append(box)

    
    for stack in starting:
        print(stack.pop())

def main():
    print("Puzzle 1 Solution: ")
    puzzle1()
    print("Puzzle 2 Solution: ")
    puzzle2() 

if __name__ == "__main__":
    puzzle1()
    puzzle2()