

def run_part1():
    start = 50
    current = start
    numberOfZeroes = 0
    with open("input.txt", "r") as f:
        for line in f:
            line_stripped = line.strip()
            direction = line_stripped[0:1]
            value = int(line_stripped[1:])
            

            remainder = value % 100
            
            mult = remainder * 1 if direction == "R" else remainder * -1
            
            if mult + current > 99:
                # at 97, move 4 to the right, should be at 1
                current = ((mult + current) - 99)-1
            elif mult + current < 0:
                # at 2, move 4 to the left, should be at 98
                current = (99 + (mult + current))+1
            else:
                current = mult+current
            
            # print(current)

            if current == 0:
               
                numberOfZeroes = numberOfZeroes + 1
        
    print(numberOfZeroes)

def run_part2():
    start = 50
    current = start
    numberOfZeroesCrossed = 0
    with open("input.txt", "r") as f:
        for line in f:
            line_stripped = line.strip()
            direction = line_stripped[0:1]
            value = int(line_stripped[1:])

            remainder = value % 100
            numberOfHundreds = value // 100
            numberOfZeroesCrossed = numberOfZeroesCrossed + numberOfHundreds
            
            mult = remainder * 1 if direction == "R" else remainder * -1
            
            if mult + current > 100:
                # at 97, move 4 to the right, should be at 1
                current = ((mult + current) - 99)-1
                numberOfZeroesCrossed = numberOfZeroesCrossed + 1
            elif mult + current < 0:
                # at 2, move 4 to the left, should be at 98
                currentStart = current
                current = (99 + (mult + current))+1
                if currentStart != 0:
                    numberOfZeroesCrossed = numberOfZeroesCrossed + 1
            elif mult + current == 100 or mult + current == 0:
                current = 0
                numberOfZeroesCrossed = numberOfZeroesCrossed + 1
            else:
                current = mult+current
        
    print(numberOfZeroesCrossed)

if __name__ == "__main__":
    run_part2()