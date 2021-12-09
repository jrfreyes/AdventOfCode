
class Submarine:
    def __init__(self) -> None:
        self.depth = 0
        self.pos = 0
        self.aim = 0
    
    def move(self, command):
        direction, magnitude = command.split()
        magnitude = int(magnitude)
        if direction == 'forward':
            self.pos += magnitude
        elif direction == 'down':
            self.depth += magnitude
        else:
            self.depth -= magnitude

    def move_aim(self, command):
        direction, magnitude = command.split()
        magnitude = int(magnitude)
        if direction == 'forward':
            self.pos += magnitude
            self.depth += self.aim * magnitude
        elif direction == 'down':
            self.aim += magnitude
        else:
            self.aim -= magnitude

    def __str__(self) -> str:
        return f'Depth: {self.depth} Pos: {self.pos}'

def main():
    sub = Submarine()
    with open('input') as f:
        commands = [command for command in f]
    list(map(sub.move, commands))
    print(sub.depth * sub.pos)
    sub2 = Submarine()
    list(map(sub2.move_aim, commands))
    print(sub2.depth * sub2.pos)
    

if __name__ == '__main__':
    main()