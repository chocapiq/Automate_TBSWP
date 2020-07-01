grid_cheat_sheet = [['00', '01'],
                    ['10', '11']]

grid1 = [['.', '.', '.', '.', '.', '.'],
         ['.', 'O', 'O', '.', '.', '.'],
         ['O', 'O', 'O', 'O', '.', '.'],
         ['O', 'O', 'O', 'O', 'O', '.'],
         ['.', 'O', 'O', 'O', 'O', 'O'],
         ['O', 'O', 'O', 'O', 'O', '.'],
         ['O', 'O', 'O', 'O', '.', '.'],
         ['.', 'O', 'O', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.']]

grid2 = [['.', '.', '.', '.', '.', '.'],
         ['.', 'O', 'O', '.', '.', '.'],
         ['O', 'O', 'O', 'O', '.', '.'],
         ['O', 'O', 'O', 'O', 'O', '.'],
         ['.', 'O', 'O', 'O', 'O', 'O'],
         ['.', '.', '.', '.', '.', ''],
         ['', '', '', '', '', '.'],
         ['.', '.', '.', '.', '.', ''],
         ['.', '.', '.', '', '', ''],
         ['', '', '.', '', '', ''],
         ['.', '.', '.', '', '', '']]

def GridPrinter(grid):
        x = 0
        y = 0
        z = 1
        gridX = len(grid)
        gridY = len(grid[1])

        while x <= gridX + 1:
                if x == gridX:
                        x = 0
                        y += 1
                        while y <= gridY:
                                if z == 1:
                                        print('', end='\n')
                                if x == gridX or y == gridY:
                                        z = 1
                                        break
                                else:
                                        print(grid[x][y], end='')
                                        x += 1
                                        z += 1

                elif y < gridY:
                        print(grid[x][y], end='')
                        x += 1
                else:
                        break

GridPrinter(tableData)