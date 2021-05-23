


class BitmaskSystem:
    @staticmethod
    def apply_mask(val, mask):
        bitmask = {i:int(x) for i, x in enumerate(mask[::-1]) if x.isnumeric()}

        for i in bitmask:
            if bitmask[i]:
                val |= 1 << i
            else:
                #val = ~(~val | (1 << i))
                val &= ~(1 << i)

        return val
    
    @staticmethod
    def decode_address(addr, mask):
        floating_bits = [i for i, x in enumerate(mask) if x == 'X']
        n = 2 ** len(floating_bits)
        
        # first, apply the 1s in the bit mask     
        for i, x in enumerate(mask[::-1]):
            if x == '1':
                addr |= 1 << i

        if n == 0:
            return (addr,)

        # create new bitmasks to be used to the apply_bitmask function
        new_bitmask = 'X'*len(mask)
        masks = [new_bitmask] * n

        for i in range(n):
            mask_bits = f'{i:0{len(floating_bits)}b}'
            for j, bit in zip(floating_bits, mask_bits):
                masks[i] = masks[i][:j] + bit + masks[i][j+1:]
        
        return tuple(BitmaskSystem.apply_mask(addr, m) for m in masks)
        

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
            addrs = BitmaskSystem.decode_address(addr, self.mask)
            val = int(val.strip())
            for a in addrs:
                self.mem[a] = val
        self.curr += 1
        return inst, val

    def get_sum(self):
        return sum(self.mem.values())

    def is_eof(self):
        return self.curr >= len(self.instructions)

    

if __name__ == '__main__':
    apply_mask = BitmaskSystem.apply_mask
    decode_addr = BitmaskSystem.decode_address
    print(apply_mask(11, 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'))
    mask = '000000000000000000000000000000X1001X'
    print(decode_addr(42, mask))
    mask = '00000000000000000000000000000000X0XX'
    print(decode_addr(26, mask))

    bms = BitmaskSystem('test2')
    while not bms.is_eof():
        bms.step()
    print(f'Sum: {bms.get_sum()}')
    
    bms = BitmaskSystem('input')
    while not bms.is_eof():
        bms.step()
    print(f'Sum: {bms.get_sum()}')
