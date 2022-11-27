class Solver:
    def __init__(self, game):
        self.path = []
        self.game = game

    def misplaced_tiles(self):
        return len([1 for i in range(self.game.game_size) for j in range(self.game.game_size) if
                    self.game.tiles_grid[i][j] != i * self.game.game_size + j + 1 and self.game.tiles_grid[i][j] != 0])

    def distance(self):
        return sum([abs(self.game.tiles_grid[i][j] - (i * self.game.game_size + j + 1)) for i in range(self.game.game_size) for j in
                    range(self.game.game_size) if self.game.tiles_grid[i][j] != 0])

    def greedy(self, moves):
        cost = []
        for move in moves:
                cost.append((self.distance(), move))
                self.path.append(move)

        return min(cost)[1]


    def solve(self):
        print("Solving...")
        print("Misplaced tiles: ", self.misplaced_tiles())
        print("Distance: ", self.distance())
        print("Grid: ", self.game.tiles_grid)

