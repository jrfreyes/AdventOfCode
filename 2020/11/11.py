import copy

class Seating:
    def __init__(self, file) -> None:
        self._stable = False
        self.seats = []
        self.n_steps = 0 
        self._load_file(file)

    def _load_file(self, file):
        with open(file) as f:
            self.seats = [list(line.strip()) for line in f if not line.isspace()]
        self.height = len(self.seats)
        self.width = len(self.seats[0])

    def _get_next_state_part_one(self, x, y) -> str:
        '''Returns the next state of a given seat'''
        seat_state = self.seats[y][x]
        if seat_state == '.':
            return seat_state
        neighbors = self.get_neighbors(x, y)
        
        # if empty check if neighbors are not occupied
        if seat_state == 'L' and '#' not in neighbors:
            return '#'
        
        # if occupied check if four or more neighbors are occupied
        if seat_state == '#' and neighbors.count('#') >= 4:
            return 'L'

        return seat_state
    
    def _get_next_state_part_two(self, x, y) -> str:
        '''Returns the next state of a given seat'''
        seat_state = self.seats[y][x]
        if seat_state == '.':
            return seat_state
        visible_seats = self.get_visible_seats(x, y)
        
        # if empty check if neighbors are not occupied
        if seat_state == 'L' and '#' not in visible_seats:
            return '#'
        
        # if occupied check if five or more neighbors are occupied
        if seat_state == '#' and visible_seats.count('#') >= 5:
            return 'L'

        return seat_state

    def get_neighbors(self, x, y) -> list:
        '''Returns the list of neighbors of a given seat'''
        neighbors = list()
        on_left_edge = (x == 0)
        on_top_edge = (y == 0)
        on_right_edge = (x == len(self.seats[0]) - 1)
        on_bottom_edge = (y == len(self.seats) - 1)

        if not on_left_edge:
            neighbors.append(self.seats[y][x - 1])
            if not on_top_edge:
                neighbors.append(self.seats[y - 1][x - 1])
        
        if not on_top_edge:
            neighbors.append(self.seats[y - 1][x])
            if not on_right_edge:
                neighbors.append(self.seats[y - 1][x + 1])
            
        if not on_right_edge:
            neighbors.append(self.seats[y][x + 1])
            if not on_bottom_edge:
                neighbors.append(self.seats[y + 1][x + 1])

        if not on_bottom_edge:
            neighbors.append(self.seats[y + 1][x])
            if not on_left_edge:
                neighbors.append(self.seats[y + 1][x - 1])
        return neighbors

    def get_visible_seats(self, x, y):
        visible_seats = list()

        for dir_y in range(-1,2):
            for dir_x in range(-1,2):
                if dir_x == 0 and dir_y == 0:
                    continue
                seek_y = y + dir_y
                seek_x = x + dir_x
                while all((seek_x >= 0, seek_x < self.width,
                           seek_y >= 0, seek_y < self.height)):
                    if self.seats[seek_y][seek_x] in 'L#':
                        visible_seats.append(self.seats[seek_y][seek_x])
                        break
                    seek_x += dir_x
                    seek_y += dir_y
        return visible_seats


    def step(self, part = 2):
        if part == 1:
            get_next_state = self._get_next_state_part_one
        elif part == 2:
            get_next_state = self._get_next_state_part_two
        changed = False
        new_seats = copy.deepcopy(self.seats)
        for y in range(len(self.seats)):
            for x in range(len(self.seats[y])):
                next_state = get_next_state(x, y)
                if self.seats[y][x] != next_state:
                    new_seats[y][x] = next_state
                    changed = True
        self._stable = not changed
        self.seats = new_seats
        self.n_steps += 1
        return self

    def is_stable(self) -> bool:
        return self._stable

    def count(self, state: str) -> int:
        return sum(row.count(state) for row in self.seats)

    def __str__(self) -> str:
        return '\n'.join(''.join(seat) for seat in self.seats)

if __name__ == '__main__':
    s = Seating('test')
    with open('test2') as f:
        test_raw = f.read()
    tests = [state.strip() for state in test_raw.split('\n\n')]
    while s.n_steps < 2:
        s.step()
    print(s)
    while not s.is_stable():
        assert str(s) == tests[s.n_steps], f"Failed at step {s.n_steps}"
        s.step()
    print(s)
    print(f'Stable in {s.n_steps}')
    print(s.count('#'))

    s1 = Seating('input')
    print(s1)
    while not s1.is_stable():
        s1.step()
    print(s1)
    print(f'Stable in {s1.n_steps} steps')
    print(s1.count('#'))
