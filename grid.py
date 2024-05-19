import numpy as np
import math

class Grid:
    def __init__(self, row: int, col: int) -> None:
        self._r = row
        self._c = col
        self.grid = np.empty((0, self._c), dtype=int)
    
    def __getitem__(self, index):
        r, c = index
        return self.grid[r, c]

    def __len__(self):
        return len(self.grid)

    def populate(self) -> None:
        for _ in range(self._r):
            new_row = self._gen_stars(self._c)
            if len(new_row) != self._c:
                raise ValueError(f"The length of generated row must match the length of column ({self._c})")
            self.grid = np.vstack((self.grid, new_row))

    def update(self, direction) -> None: # 1 up, -1 down, 2 left, -2 right 
        n_galaxies = np.random.default_rng().integers(0, 2)
        length_flag = np.random.choice([True, False], p=[0.95, 0.05])
        match direction:
            case 1:
                new_row = self._gen_stars(self._c)
                self.grid = np.vstack((new_row, self.grid))
                self.grid = np.delete(self.grid, (self._r), axis = 0)
                self._gen_galaxies(n_galaxies, [(-1, 0), (-1, 1), (-1, -1)], 1, len(new_row), self.grid[1], length_flag)
            case -1:
                new_row = self._gen_stars(self._c)
                self.grid = np.vstack((self.grid, new_row))
                self.grid = np.delete(self.grid, (0), axis = 0)
                self._gen_galaxies(n_galaxies, [(1, 0), (1, -1), (1, 1)], -1, len(new_row), self.grid[-2], length_flag) 
            case 2:
                new_col = self._gen_stars(self._r)
                self.grid = np.hstack((new_col[:, np.newaxis], self.grid))
                self.grid = np.delete(self.grid, (self._c), axis = 1)
                self._gen_galaxies(n_galaxies, [(0, -1), (-1, -1), (1, -1)], 2, len(new_col), self.grid[:, 1], length_flag)
            case -2:
                new_col = self._gen_stars(self._r)
                self.grid = np.hstack((self.grid, new_col[:, np.newaxis]))
                self.grid = np.delete(self.grid, (0), axis = 1)
                self._gen_galaxies(n_galaxies, [(0, 1), (1, 1), (-1, 1)], -2, len(new_col), self.grid[:, -2], length_flag)
                
    def _gen_galaxies(self, n: int, directions: list, move: int, length_new, prior_env: list, length: bool) -> None:
        if not any(element == 2 for element in prior_env):
            galaxies_coords = self._rand_coords(n, move, math.floor(length_new * 1/5)) 
            for coords in galaxies_coords:
                self.grid[coords[0], coords[1]] = 2
        else:
            if length:
                for index, element in enumerate(prior_env):
                    rand_directions_index = np.random.random_integers(0, (len(directions) - 1))
                    rand_directions = directions[rand_directions_index]
                    element_r = 0
                    element_c = 0
                    if element == 2:
                        match move:
                            case 1:
                                element_r, element_c = 1, index 
                            case -1:
                                element_r, element_c = self._r - 2, index
                            case 2:
                                element_r, element_c = index, 1
                            case -2:
                                element_r, element_c = index, self._c - 2
                        
                        next_row = element_r + rand_directions[0]
                        next_col = element_c + rand_directions[1]
                        if 0 <= next_row < self._r and 0 <= next_col < self._c:
                            self.grid[next_row, next_col] = 2
                            
    def _gen_stars(self, size: int) -> np.array:
        rng = np.random.default_rng()
        stars_arr = np.zeros(size, dtype=int)
        n_stars = rng.integers(0, np.ceil(size * 0.01))
        while n_stars > 0:
            i = rng.integers(0, size - 1)
            if stars_arr[i] == 0:
                if stars_arr[i-1] == 0:
                    if stars_arr[i+1] == 0:
                        stars_arr[i] = 1
                        n_stars -= 1
        return stars_arr
    
    def _rand_coords(self, n_pairs: int, move: int, min_sep: int) -> list: 
        rng = np.random.default_rng()
        used_coordinates = []
        count_pairs = 0

        while count_pairs < n_pairs:
            rand_coordate = None
            match move:
                case 1:
                    rand_coordate = (0, rng.integers(0, self._c))
                case -1:
                    rand_coordate = (self._r - 1, rng.integers(0, self._c))
                case 2:
                    rand_coordate = (rng.integers(0, self._r), 0)
                case -2:
                    rand_coordate = (rng.integers(0, self._r), self._c - 1)
                
            if all(np.linalg.norm(np.array(used_coord) - np.array(rand_coordate)) >= min_sep for used_coord in used_coordinates):
                used_coordinates.append(rand_coordate)
                count_pairs += 1
        
        return used_coordinates