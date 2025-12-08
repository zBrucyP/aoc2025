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


def tachyon_pathfinder(total: int, current_path_diagram: list[list[str]], start_row_idx: int, start_col_idx: int, saved_paths: dict):
    if start_row_idx == len(current_path_diagram)-1:
        return total + 1
    
    # original solution too inefficient for big input, need to save what we've seen before
    saved_key = f"{start_row_idx},{start_col_idx}"
    if saved_key in saved_paths:
        return total + saved_paths[saved_key]

    row_idx = start_row_idx
    next_row_val = current_path_diagram[start_row_idx+1][start_col_idx]
    while row_idx < len(current_path_diagram):
        # fill path downwards until hit a split
        if row_idx < len(current_path_diagram)-1:
            next_row_val = current_path_diagram[row_idx+1][start_col_idx]
        if next_row_val == "^": # hit a split
            break
        row_idx += 1

    next_paths = 0
    if next_row_val == "^" and row_idx + 1 < len(current_path_diagram):
        # at split, recurse left and right
        if start_col_idx - 1 >= 0 and current_path_diagram[row_idx+1][start_col_idx-1] != "^":
            # left
            next_paths += tachyon_pathfinder(total, current_path_diagram, row_idx+1, start_col_idx-1, saved_paths)
        if start_col_idx + 1 < len(current_path_diagram[0]) and current_path_diagram[row_idx+1][start_col_idx+1] != "^":
            # right
            next_paths += tachyon_pathfinder(total, current_path_diagram, row_idx+1, start_col_idx+1, saved_paths)
    elif row_idx >= len(current_path_diagram) - 1:
        next_paths = 1
    
    saved_paths[saved_key] = next_paths
    return total + next_paths



def run():
    diagram: list[list[str]] = []
    with open("input.txt") as file:
        for line in file:
            row = list(line.strip())
            diagram.append(row)

    # part 1    
    # new_diagram, splits = simulate_tachyon(diagram=diagram)
    # print(f"splits: {splits}")

    # part 2
    s_row_idx = 1 # start in row below S
    s_col_idx = diagram[0].index("S")
    total_paths = tachyon_pathfinder(0, diagram, s_row_idx, s_col_idx, saved_paths={})
    # print("all path diagrams:")
    # for path_diagram in all_path_diagrams:
    #     for row in path_diagram:
    #         print("".join(row))
    #     print("____________________________")
    #     print("____________________________")
    print(f"number of paths: {total_paths}")

if __name__ == "__main__":
    run()


# 3138 your answer is too low