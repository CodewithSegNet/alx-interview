#!/usr/bin/python3

def island_perimeter(grid):
    if not grid:
        return 0

    '''
    initialize perimeter
    '''
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    '''
    iterate through the rows of grid
    '''
    for row in range(rows):
        '''
        iterate through the cols or grid
        '''
        for col in range(cols):
            if grid[row][col] == 1:
                '''
                count the perimeter for this land cell
                and initialize with 6 edges
                '''
                perimeter += 4

                '''
                checking (up, down, left, right) cell
                '''
                if row > 0 and grid[row - 1][col] == 1:
                    '''
                    subtract 1 for each shared edge (UP)
                    '''
                    perimeter -= 1
                if row < rows - 1 and grid[row + 1][col] == 1:
                    '''
                    (DOWN)
                    '''
                    perimeter -= 1
                if col > 0 and grid[row][col - 1] == 1:
                    '''
                    (LEFT)
                    '''
                    perimeter -= 1
                if col < cols - 1 and grid[row][col + 1] == 1:
                    '''
                    (RIGHT)
                    '''
                    perimeter -= 1

    return perimeter
