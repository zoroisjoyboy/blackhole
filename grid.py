import numpy as np

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

    def update(self, direction) -> None: # call vstack or hstack depending on direction 
        pass

    def random_ascii(self):
        n = np.random.default_rng().integers(97, 122)
        return chr(n)
    
    def _gen_galaxies(self) -> None:
        pass

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
    





            
        

