
def is_coordinate_accessible(paper_map: list[list[str]], i: int, j: int) -> bool:
    # extracted shared function for part 1 and 2
    row_length = len(paper_map[0])
    surrounding_rolls = 0
    # right
    if j + 1 < row_length and paper_map[i][j + 1] == "@":
        surrounding_rolls += 1
    # left
    if j - 1 >= 0 and paper_map[i][j - 1] == "@":
        surrounding_rolls += 1
    #down
    if i + 1 < len(paper_map) and paper_map[i + 1][j] == "@":
        surrounding_rolls += 1
    #  up
    if i - 1 >= 0 and paper_map[i - 1][j] == "@":
        surrounding_rolls += 1
    # up left
    if i - 1 >= 0 and j - 1 >= 0 and paper_map[i - 1][j - 1] == "@":
        surrounding_rolls += 1
    # up right
    if i - 1 >= 0 and j + 1 < row_length and paper_map[i - 1][j + 1] == "@":
        surrounding_rolls += 1
    # down left
    if i + 1 < len(paper_map) and j - 1 >= 0 and paper_map[i + 1][j - 1] == "@":
        surrounding_rolls += 1
    # down right
    if i + 1 < len(paper_map) and j + 1 < row_length and paper_map[i + 1][j + 1] == "@":
        surrounding_rolls += 1
    
    
    return surrounding_rolls < 4


def accessible_rolls_v1(paper_map: list[list[str]]) -> int:
    row_length = len(paper_map[0])
    accessible_rolls = 0
    for i, row, in enumerate(paper_map):
        for j, cell in enumerate(row):
            if cell == "@":
                if is_coordinate_accessible(paper_map, i, j):
                    accessible_rolls += 1

    return accessible_rolls


def remove_accessible_rows(paper_map: list[list[str]]):
    # returns list[list[str]], int -> new map, number of removed rolls
    row_length = len(paper_map[0])
    removed_rolls = 0
    for i, row, in enumerate(paper_map):
        for j, cell in enumerate(row):
            if cell == "@":
                if is_coordinate_accessible(paper_map, i, j):
                    removed_rolls += 1
                    paper_map[i][j] = "."
    return paper_map, removed_rolls



def run_v1():
    with open("input.txt", "r") as f:
        paper_map: list[list[str]] = []
        for line in f:
            paper_map.append(list(line.strip()))

        print(accessible_rolls_v1(paper_map))

def run_v2():
    with open("input.txt", "r") as f:
        paper_map: list[list[str]] = []
        for line in f:
            paper_map.append(list(line.strip()))

        total_removed = 0
        while True:
            paper_map, removed_rolls = remove_accessible_rows(paper_map)
            total_removed += removed_rolls
            if removed_rolls == 0:
                break

        print(total_removed)

if __name__ == "__main__":
    run_v2()