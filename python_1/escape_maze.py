# Each row is a list; 0 = empty space, 1 = wall, 'E' = exit
maze = [
    [0, 1, 0, 0, 'E'],
    [0, 1, 0, 1, 1],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

# Player starting position (bottom-left corner)
player_pos = (4, 0)  # row 4, column 0
def print_maze(maze, player_pos):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if (row, col) == player_pos:
                print("P", end=" ")
            elif maze[row][col] == 1:
                print("#", end=" ")
            elif maze[row][col] == 'E':
                print("E", end=" ")
            else:
                print(".", end=" ")
        print()
def move_player(player_pos, direction, maze):
    row, col = player_pos
    if direction == 'W':
        row -= 1
    elif direction == 'S':
        row += 1
    elif direction == 'A':
        col -= 1
    elif direction == 'D':
        col += 1
    else:
        print("Invalid move. Use W/A/S/D.")
        return player_pos

    # Check for wall or out of bounds
    if row < 0 or row >= len(maze) or col < 0 or col >= len(maze[0]):
        print("You hit a wall!")
        return player_pos
    elif maze[row][col] == 1:
        print("You ran into a wall!")
        return player_pos
    else:
        return (row, col)
def main():
    maze = [
        [0, 1, 0, 0, 'E'],
        [0, 1, 0, 1, 1],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    player_pos = (4, 0)
    print("Escape the Maze! Use W/A/S/D to move. Reach 'E' to win.\n")

    while True:
        print_maze(maze, player_pos)
        move = input("Move (W/A/S/D): ").upper()
        player_pos = move_player(player_pos, move, maze)

        row, col = player_pos
        if maze[row][col] == 'E':
            print("🎉 You escaped the maze! Well done!")
            break
if __name__ == "__main__":
    main()