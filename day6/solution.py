def puzzle1():

    answer = 0
    window = [ 1, 1, 1 ,'j' ]
    message = []
    marker_found = False
    with open('./day6/input.txt') as f:
        while True:
            char = f.read(1)
            answer += 1
            if not char:
                break

            if not marker_found:
                window = window[1:] + list(char)
                
            else:
                if not len(message) == 14:
                    message.append(char)
                else:
                    message = message[1:] + list(char)

                if len(set(message)) == 14:
                    print(answer)
                    break

            if len(set(window)) == 4 and not marker_found:
                print(answer)
                marker_found = True

def puzzle2():
   print('fucked up and forgot to do part 2 here, too lazy to fix')

def main():
    print("Puzzle 1 Solution: ")
    puzzle1()
    print("Puzzle 2 Solution: ")
    puzzle2() 

if __name__ == "__main__":
    main()