import heapq
import random
import time
from copy import deepcopy


class Solver:
    def __init__(self, game):
        self.path = []
        self.game = game
        self.visited = []
        self.frontier = []
        self.heuristic = self.misplaced_tiles

    def misplaced_tiles(self, tiles_grid):
        return len([1 for i in range(self.game.game_size) for j in range(self.game.game_size) if
                    tiles_grid[i][j] != i * self.game.game_size + j + 1 and tiles_grid[i][j] != 0])

    def distance(self, tiles_grid):
        return sum([abs(tiles_grid[i][j] - (i * self.game.game_size + j + 1)) for i in range(self.game.game_size) for j in
                    range(self.game.game_size) if tiles_grid[i][j] != 0])

    def selector(self, moves):

        for move in moves:
            grid = deepcopy(self.game.tiles_grid)
            if (move , grid) not in self.visited:
                candinate = self.game.move(move)
                cost = self.heuristic(candinate)
                if (cost , (move, grid)) not in self.frontier:
                    self.frontier.append((cost, (move, grid)))
                # else:
                #     prev = self.frontier.index((cost, (move, grid)))
                #     if cost < self.frontier[prev][0]:
                #         self.frontier[prev] = cost

        self.frontier = sorted(self.frontier, key=lambda x: x[0])
        print("Frontier", len(self.frontier))
        print("frontier", self.frontier)
        print("Visited", len(self.visited))
        print("visited", self.visited)
        c, s = self.frontier.pop(0)[1]
        self.visited.append((c, s))
        return c, s


    def solve(self):
        print("Solving...")


    # def get_heuristic(self, text):
    #     if text == "Misplaced":
    #         self.heuristic = self.misplaced_tiles
    #         print("Misplaced tiles heuristic selected")
    #         print(self.heuristic)
    #     elif text == "Distance":
    #         self.heuristic = self.distance


