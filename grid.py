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

    def __repr__(self) -> str:
        pass

    def populate(self) -> None:
        for _ in range(self._r):
            new_row = self._gen_stars(self._c)
            if len(new_row) != self._c:
                raise ValueError(f"The length of generated row must match the length of column ({self._c})")
            self.grid = np.vstack((self.grid, new_row))
        self._gen_blackhole()
        self._gen_galaxies()

    def update(self, direction) -> None: # 1 up, -1 down, 2 left, -2 right 
        if direction == 1 or direction == -1:
            new_row = self._gen_stars(self._c)
            if direction == 1:
                self.grid = np.vstack((new_row, self.grid))
                self.grid = np.delete(self.grid, (self._r - 1), axis = 0)
            else:
                self.grid = np.vstack((self.grid, new_row))
                self.grid = np.delete(self.grid, (0), axis = 0)
        else:
            new_col = self._gen_stars(self._r)
            if direction == 2:
                self.grid = np.hstack((new_col[:, np.newaxis], self.grid))
                self.grid = np.delete(self.grid, (self._c - 1), axis = 1)
            else:
                self.grid = np.hstack((self.grid, new_col[:, np.newaxis]))
                self.grid = np.delete(self.grid, (0), axis = 1)

    def random_ascii(self):
        n = np.random.default_rng().integers(97, 122)
        return chr(n)
    
    def _gen_galaxies(self) -> None:
        galaxies_coords = self._rand_coords(2, math.floor(self._r * 2/5))
        for coords in galaxies_coords:
            self.grid[coords[0], coords[1]] = 2
        
        def adj_helper(coord_row: list, coord_col: list) -> int:
            curr_row, curr_col = coord_row, coord_col
            length = 0
            while 0 <= curr_row < len(self.grid) and 0 <= coord_col < len(self.grid[0]) and length <= np.random.randint(self._r * 0.10, self._r * 50):    
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1)]
                rand_directions = [np.random.choice(move) for move in directions]
                next_row = curr_row + rand_directions[0]
                next_col = curr_col + rand_directions[1]

                if 0 <= next_row < len(self.grid) and 0 <= next_col < len(self.grid[0]):
                    curr_row, curr_col = next_row, next_col
                    self.grid[curr_row, curr_col] = 2
                    length += 1
                else:
                    break

            return length
            
        coords1, coords2 = galaxies_coords[0], galaxies_coords[1]
        adj_helper(coords1[0],  coords1[1]), adj_helper(coords2[0], coords2[1])

        # now take the length and build the bulb which dependant on the length
                                
    def _gen_blackhole(self) -> None: 
        center_x, center_y = (self._r // 2, self._c // 2)
        radius = math.floor(self._r * 1/5) // 2

        for x in range(len(self.grid[0])):
            for y in range(len(self.grid[1])):
                if (x - center_x) ** 2 + (y - center_y) ** 2 < radius ** 2:
                    self.grid[x, y] = 3

    def _gen_stars(self, size: int) -> np.array: 
        rng = np.random.default_rng() 
        stars_arr = np.zeros(size, dtype=int)
        n_stars = rng.integers(0, np.floor(size * 0.01))
        while n_stars > 0:
            i = rng.integers(0, size - 1)
            if stars_arr[i] == 0:
                if stars_arr[i-1] == 0:
                    if stars_arr[i+1] == 0:
                        stars_arr[i] = 1
                        n_stars -= 1
        return stars_arr
    
    def _rand_coords(self, n_pairs: int, min_sep: int) -> list: 
        rng = np.random.default_rng()
        used_coordinates = []
        count_pairs = 0
        
        while count_pairs < n_pairs:
            rand_coordate = (rng.integers(0, self._r), rng.integers(0, self._c))

            if all(np.linalg.norm(np.array(used_coord) - np.array(rand_coordate)) >= min_sep for used_coord in used_coordinates):
                used_coordinates.append(rand_coordate)
                count_pairs += 1
        
        return used_coordinates





            
        

