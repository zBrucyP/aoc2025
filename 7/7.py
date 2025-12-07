import copy

def simulate_tachyon(diagram: list[list[str]]):
    # returns final simulated diagram, number of splits
    diagram_copy = copy.deepcopy(diagram)
    row_idx = 0
    splits = 0
    while row_idx != len(diagram_copy)-1:
        for col_idx, column in enumerate(diagram_copy[row_idx]):
            current_char = diagram_copy[row_idx][col_idx]
            below_char = diagram_copy[row_idx+1][col_idx]
            if row_idx == 0 and current_char == "S":
                # find S, set up beam
                diagram_copy[row_idx+1][col_idx] = "|"
                break
            previous_char = diagram_copy[row_idx-1][col_idx]
            if current_char == "|" and below_char != "^":
                diagram_copy[row_idx+1][col_idx] = "|"
            if current_char == "^" and diagram_copy[row_idx-1][col_idx] == "|":
                splits += 1
                if col_idx - 1 >= 0 and diagram_copy[row_idx][col_idx-1] != "^":
                    diagram_copy[row_idx][col_idx-1] = "|"
                if col_idx + 1 < len(diagram_copy[0]) and diagram_copy[row_idx][col_idx+1] != "^":
                    diagram_copy[row_idx][col_idx+1] = "|"
            if current_char == "." and previous_char == "|":
                diagram_copy[row_idx][col_idx] = "|"

        row_idx += 1

    return diagram_copy, splits
                



def run_1():
    diagram: list[list[str]] = []
    with open("input.txt") as file:
        for line in file:
            row = list(line.strip())
            diagram.append(row)
    
    new_diagram, splits = simulate_tachyon(diagram=diagram)
    print(f"splits: {splits}")

if __name__ == "__main__":
    run_1()