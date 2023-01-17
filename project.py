def find_path(jungle, visited, row, col, path):
    # base case: we have reached the end of the jungle
    if col == len(jungle[0]) - 1:
        return path + [(row, col)]

    # mark the current position as visited
    visited[row][col] = True

    # explore the different directions
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for r_offset, c_offset in directions:
        new_row = row + r_offset
        new_col = col + c_offset
        if 0 <= new_row < len(jungle) and 0 <= new_col < len(jungle[0]) and jungle[new_row][new_col] == 'O' \
                and not visited[new_row][new_col]:
            visited[new_row][new_col] = True
            result = find_path(jungle, visited, new_row, new_col, path + [(row, col)])
            if result is not None:
                return result
            visited[new_row][new_col] = False

    # no path was found, so return None
    return None


def find_path_through_jungle(jungle):
    # create a 2D list to mark the visited positions
    visited = [[False for _ in row] for row in jungle]

    for row in range(len(jungle)):
        if jungle[row][0] == 'O':
            path = find_path(jungle, visited, row, 0, [])
            if path is not None:
                return path
    return None


def show_directions(jungle):
    path = find_path_through_jungle(jungle)
    if path is None:
        print("Path has not been found!")
        return

    prev_dir = "right"
    count = 0
    row = path[0][0]
    col = 0
    for r, c in path:
        if c == 0:
            continue
        if r == row:
            if c > col:
                cur_dir = "right"
                count += 1
            else:
                cur_dir = "left"
                count += 1
        elif r > row:
            cur_dir = "down"
            count += 1
            row = r
        else:
            cur_dir = "up"
            count += 1
            row = r
        col = c
        if cur_dir != prev_dir:
            print("Move", prev_dir, count - 1, "step")
            count = 1
            prev_dir = cur_dir
    print("Move", prev_dir, count, "step")


def read_data():
    file = open("data.txt", "r")
    data = []
    for i in range(24):
        data.append(file.readline().strip())
    return data


# test the function
show_directions(read_data())
