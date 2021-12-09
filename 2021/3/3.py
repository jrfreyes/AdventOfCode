def PartOne(inputs):
    n = len(inputs)
    bit_length = len(inputs[0])

    sums = [0] * bit_length
    for line in inputs:
        for i in range(bit_length):
            sums[i] += int(line[i])
    gamma = int(''.join([str(round(x/n)) for x in sums]), 2)
    epsilon = gamma ^ ((1 << bit_length) - 1)

    return gamma * epsilon

def PartTwo(inputs):
    n = len(inputs)
    bit_length = len(inputs[0])

    zeroes = []
    ones = []
    oxy = inputs
    for i in range(bit_length):
        for num in oxy:
            if num[i] == '0':
                zeroes.append(num)
            else:
                ones.append(num)
        oxy = ones if len(ones) >= len(zeroes) else zeroes
        zeroes = []
        ones = []
        if len(oxy) == 1:
            oxy_rate = int(oxy[0], 2)
            break
    co2 = inputs
    for i in range(bit_length):
        for num in co2:
            if num[i] == '0':
                zeroes.append(num)
            else:
                ones.append(num)
        co2 = zeroes if len(ones) >= len(zeroes) else ones
        zeroes = []
        ones = []
        if len(co2) == 1:
            co2_rate = int(co2[0], 2)
            break
    
        

    return oxy_rate * co2_rate


def main():
    with open('input') as f:
        inputs = [line.strip() for line in f]
    with open('test') as f:
        test = [line.strip() for line in f]
    
    print(PartOne(inputs))
    print(PartTwo(inputs))
if __name__ == '__main__':
    main()