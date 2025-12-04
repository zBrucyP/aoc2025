import time

def get_max_joltage_bad(bankString: str) -> str:
    #The batteries are arranged into banks; each line of digits in your input 
    # corresponds to a single bank of batteries. Within each bank, you need to
    #  turn on exactly two batteries; the joltage that the bank produces is equal
    #  to the number formed by the digits on the batteries you've turned on. 
    # For example, if you have a bank like 12345 and you turn on batteries 2 and 4, 
    # the bank would produce 24 jolts. (You cannot rearrange batteries.)
    bank_sorted = sorted(bankString)
    max = bank_sorted[-1]
    second_max = bank_sorted[-2]
    for char in bankString:
        if char == max:
            return max + second_max
        elif char == second_max:
            return second_max + max
    return 0

def get_max_joltage_v1(bankString: str) -> str:
    max_joltage = 0
    bankLength = len(bankString)
    for i in range(bankLength):
        for j in range(i + 1, bankLength):
            joltage = int(bankString[i] + bankString[j])
            if joltage > max_joltage:
                max_joltage = joltage
    return str(max_joltage)


def get_max_joltage_v2_bad(bankString: str) -> str:
    # [0,1,2,3,4]
    # 987654321111111
    # 234234234234278
    # 
    # Now, you need to make the largest joltage by turning on exactly twelve batteries within each bank.
    # The joltage output for the bank is still the number formed by the digits of the batteries you've turned on;
    #  the only difference is that now there will be 12 digits in each bank's joltage output instead of two.
    idx12FromRight = len(bankString) - 12
    maxIdxLeftOf12Idx = 0
    indexToValue = {}
    for i in range(idx12FromRight):
        if int(bankString[i]) > maxIdxLeftOf12Idx:
            maxIdxLeftOf12Idx = int(bankString[i])
            indexToValue[i] = maxIdxLeftOf12Idx

    extraSpots = len(bankString) - maxIdxLeftOf12Idx - 12
    startIdx = maxIdxLeftOf12Idx + 1

    print("Max left of idx12FromRight:", maxIdxLeftOf12Idx)
    return 0


def get_max_joltage_v2(bankString: str) -> str:
    slots = []
    lookback = 11
    startIdx = 0

    # we need 12 batteries
    while len(slots) < 12:
        # reserve at least enough space for the max remaining batteries
        idx12FromRight = len(bankString) - lookback
        # grab the substring we can evaluate
        subStringToEval = bankString[startIdx:idx12FromRight]
        # find the max in the current eval group
        maxInt, maxIdx = get_max_int_from_string(subStringToEval)
        slots.append(maxInt)
        # decrement how many more batteries we need
        lookback -= 1
        # jump the evaluation substring start to the latest max
        startIdx = startIdx + maxIdx + 1
    
    return ''.join([str(i) for i in slots])


# returns max int and its index
def get_max_int_from_string(s: str):
    max = 0
    idx = -1
    for char in s:
        if int(char) > max:
            max = int(char)
            idx = s.index(char)
    return max, idx


def run():
    max_joltages = []
    with open("input.txt") as f:
        for line in f:
            max_voltage = int(get_max_joltage_v2(line.strip()))
            max_joltages.append(max_voltage)

    print(f"Sum of max joltages: {sum(max_joltages)}")


if __name__ == "__main__":
    start = time.time()
    run()
    end = time.time()
    print("Execution time:", end - start)