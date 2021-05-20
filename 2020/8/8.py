
class Program:
    def __init__(self, file):
        with open('input') as f:
            self.instructions = [instruction.strip() for instruction in f if not instruction.isspace()]
            self.reset()

    def is_terminated(self):
        return self.current >= len(self.instructions)

    def reset(self):
        self.accumulator = 0
        self.current = 0
        self.execution_counts = [0] * len(self.instructions)
    
    def execute(self):
        while not self.is_terminated():
            self.step()

    def step(self):
        if self.is_terminated():
            raise Exception('Program already terminated')
        self.execution_counts[self.current] += 1
        opcode, val = self.parse_instruction()
        op = getattr(self, opcode)
        op(val)

    def parse_instruction(self):
        opcode, val = self.instructions[self.current].split()
        return opcode, int(val)

    def jmp(self, x):
        self.current += x

    def acc(self, x):
        self.accumulator += x
        self.jmp(1)
    
    def nop(self, x):
        self.jmp(1)

    def fix_loop(self):
        while not self.is_terminated():
            opcode, val = self.parse_instruction()
            subs  = {'jmp': 'nop', 'nop': 'jmp'}
            if opcode in subs:
                old_inst = self.instructions[self.current]

                new_inst = f'{subs[opcode]} {val:+d}'
                self.instructions[self.current] = new_inst

                if not self.is_loop():
                    self.reset()
                    return

                self.instructions[self.current] = old_inst
            self.step()

    def is_loop(self):
        accumulator = self.accumulator
        curr = self.current
        exec_counts = self.execution_counts.copy()
        self.reset()
        loop = False
        while not self.is_terminated():
            self.step()
            if self.is_terminated():
                break
            if self.execution_counts[prog.current] > 0:
                loop = True
                break
        self.accumulator = accumulator
        self.current = curr
        self.execution_counts = exec_counts
        return loop
    
if __name__ == '__main__':
    prog = Program('input')
    while prog.execution_counts[prog.current] == 0:
        prog.step()
    print(prog.accumulator)
    prog.reset()
    prog.fix_loop()
    prog.execute()
    print(prog.accumulator)