
class Ship:
    directions = {
        'N': (0,1),
        'S': (0,-1),
        'E': (1,0),
        'W': (-1,0)
    }
    def __init__(self, file) -> None:
        self._load_file(file)
        self.x = 0
        self.y = 0
        self.curr = 0
        self.waypoint = (10,1)
    
    def _load_file(self, file):
        with open(file) as f:
            self.instructions = [line.strip() for line in f if not line.isspace()]

    def step(self):
        curr_inst = self.instructions[self.curr]
        inst, val = curr_inst[0], int(curr_inst[1:])
        
        if inst in 'NSEW':
            self.move_waypoint(val, inst)
        elif inst in 'LR':
            self.rotate_waypoint(val * (1 if inst == 'R' else -1))
        elif inst == 'F':
            self.move(val)
        self.curr += 1
        return self

    def execute(self):
        while not self.is_end_of_trip():
            self.step()

    def is_end_of_trip(self):
        return self.curr >= len(self.instructions)

    def move(self, val):
        dir_x, dir_y = self.waypoint

        self.x += dir_x * val
        self.y += dir_y * val

    def move_waypoint(self, val, bearing):
        dir_x, dir_y = Ship.directions[bearing]
        x, y = self.waypoint

        x += dir_x * val
        y += dir_y * val

        self.waypoint = (x, y)


    def rotate_waypoint(self, angle):
        angle %= 360
        dir = angle // 90
        x, y = self.waypoint
        
        for i in range(dir):
            x, y = y, -x
        
        self.waypoint = (x, y)

    def get_manhattan_distance(self):
        return abs(self.x) + abs(self.y)
    
    def __str__(self):
        next_inst = self.instructions[self.curr] if self.curr < len(self.instructions) else None
        return f'x: {self.x} y: {self.y} waypoint: {self.waypoint} manhattan distance: {self.get_manhattan_distance()} next instruction: {next_inst}'

if __name__ == '__main__':
    
    test_ship = Ship('test')

    while not test_ship.is_end_of_trip():
        print(test_ship.step())

    print()

    ship = Ship('input')
    print(ship)
    while not ship.is_end_of_trip():
        print(ship.step())