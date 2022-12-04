def puzzle1():

    with open('./day4/input.txt') as f:
        lines = f.readlines()

    total = 0

    for line in lines:
        line = line.strip()
        [first, second] = line.split(',')
        first = list(map(int, first.split('-')))
        second = list(map(int, second.split('-')))

        if first[0] <= second[0] and first[1] >= second[1]:
            total += 1
        elif second[0] <= first[0] and second[1] >= first[1]:
            total += 1

    print(total)

def puzzle2():
    with open('./day4/input.txt') as f:
        lines = f.readlines()

    total = 0

    for line in lines:
        line = line.strip()
        [first, second] = line.split(',')
        first = list(map(int, first.split('-')))
        second = list(map(int, second.split('-')))


        if second[0] <= first[1] and second[0] >= first[0]:
            total += 1
        elif first[0] <= second[1] and first[0] >= second[1]:
            total += 1
        elif first[0] >= second[0] and first[0] <= second[1]:
            total += 1
        elif second[0] >= first[0] and second[0] <= first[0]:
            total += 1

    print(total)

def main():
    print("Puzzle 1 Solution: ")
    puzzle1()
    print("Puzzle 2 Solution: ")
    puzzle2() 

if __name__ == "__main__":
    main()