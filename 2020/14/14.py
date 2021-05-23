


class BitmaskSystem:
    @staticmethod
    def apply_mask(val, mask):
        bitmask = {i:int(x) for i, x in enumerate(mask[::-1]) if x.isnumeric()}

        for i in bitmask:
            if bitmask[i]:
                val |= bitmask[i] << i
            else:
                #val = ~(~val | (1 << i))
                val &= ~(1 << i)

        return val
    
    def __init__(self, file: str) -> None:
        self.mem = {}
        with open(file) as f:
            self.instructions = [line.strip() for line in f if not line.isspace()]
        self.curr = 0

    def step(self):
        inst = self.instructions[self.curr]
        if inst.isspace():
            return
        op, val = inst.split(' = ')
        if op[:4] == 'mask':
            val = val.strip()
            self.mask = val
        elif op[:3] == 'mem':
            addr = int(op[4:-1])
            val = BitmaskSystem.apply_mask(int(val.strip()),self.mask)
            self.mem[addr] = val
        self.curr += 1
        return inst, val

    def get_sum(self):
        return sum(self.mem.values())

    def is_eof(self):
        return self.curr >= len(self.instructions)

    

if __name__ == '__main__':
    apply_mask = BitmaskSystem.apply_mask
    print(apply_mask(11, 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'))
    print(apply_mask(101, 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X')) 
    print(apply_mask(0, 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'))
    
    bms = BitmaskSystem('test')
    while not bms.is_eof():
        bms.step()
    print(bms.get_sum())

    bms = BitmaskSystem('input')
    while not bms.is_eof():
        bms.step()
    print(bms.get_sum())
