import math
import time

operations = {
    '*': lambda lis: math.prod(lis),
    '+': lambda lis: sum(lis) 
}

def part_1(math_map: list[list[str]]) -> int:
    results = []
    # while len(results) < len(math_map[0]):
    for col_number, _ in enumerate(math_map[0]):
        values_in_column: list[int] = [int(math_map[row_idx][col_number]) for row_idx, _ in enumerate(math_map) if row_idx != len(math_map)-1 ]
        operation = math_map[-1][col_number]
        result = operations[operation](values_in_column)
        results.append(result)
    
    return sum(results)


def part_2(math_map: list[str]) -> int:
    # 123 328  51 64 
    #  45 64  387 23 
    #   6 98  215 314
    # *   +   *   + 
    results: list[int] = []

    column = 0
    current_operation = ''
    current_operation_values: list[int] = []
    while column < len(math_map[0])-1:
        operation_in_col = math_map[-1][column]
        if operation_in_col != ' ':
            print(f"change {operation_in_col}")
            if column != 0:
                # time to run operation
                operation = operations[current_operation]
                res = operation(current_operation_values)
                results.append(res)
            current_operation = operation_in_col
            current_operation_values = []

        # get next value
        columnar_val = ''
        for row_idx, row in enumerate(math_map):
            if column < len(row):
                val = math_map[row_idx][column]
            if val != ' ' and row_idx != len(math_map)-1:
                columnar_val += val

        if columnar_val != '':
            current_operation_values.append(int(columnar_val))

        print(current_operation_values)
        column += 1
    
    operation = operations[current_operation]
    res = operation(current_operation_values)
    results.append(res)

    print(results)

    return sum(results)
        


def run():
    problem_map: list[list[str]] = []
    with open("input.txt") as file:
        for line in file:
            # parts = split(line)
            # input is weird, remove empty strings
            # parts = [part for part in parts if part != '']
            problem_map.append(line)

    result = part_2(problem_map)
    print(f"Result: {result}")


if __name__ == "__main__":
    start_time = time.time()
    run()
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")

