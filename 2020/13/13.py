
def parse(file):
    with open(file) as f:
        timestamp = int(f.readline())
        buses = [int(x) for x in f.readline().split(',') if x.isnumeric()]
    return (timestamp, buses)

def is_departing(timestamp, bus):
    return timestamp % bus == 0

def get_next_departure(timestamp, bus):
    return (timestamp // bus + 1) * bus if timestamp % bus else timestamp

def get_earliest_bus(timestamp, buses):
    departures = [get_next_departure(timestamp, x) for x in buses]
    earliest_departure = min(departures)
    return (earliest_departure, buses[departures.index(earliest_departure)])

def parse_two(file):
    with open(file) as f:
        timestamp = int(f.readline())
        buses = {t:int(x) for t, x in enumerate(f.readline().split(',')) if x.isnumeric()}
    return buses

def product(*x):
    y = 1
    for num in x:
        y *= num
    return y

# Chinese Remainder Theorem 
# http://homepages.math.uic.edu/~leon/mcs425-s08/handouts/chinese_remainder.pdf
# https://www.youtube.com/watch?v=zIFehsBHB8o
def find_part_two(buses, t = 0):
    keys = list(buses.keys())
    a = [-key % buses[key] for key in keys]
    m = [buses[key] for key in keys]
    m_product = product(*m)
    z = [m_product // mi for mi in m]
    y = []
    for zi, mi in zip(z, m):
        yi  = 1
        while yi * zi % mi != 1:
            yi += 1
        y.append(yi)
    
    print('Keys: {}\na: {}\nm: {}:\nm_product{}\nz{}'.format(keys,a,m,m_product,z))
    print(f'y: {y}')
    x = sum(ai * yi * zi for ai, yi, zi in zip(a, y, z)) % m_product

    print(f'x ≡ {x} (mod {m_product})')

# Takes a long time
# def find_part_two(buses, t = 0):
#     first_bus = buses[0]
#     t = get_next_departure(t, first_bus)
#     while True:
#         if all(((get_next_departure(t, buses[i]) == t + i) for i in buses)):
#             return t
#         t += first_bus
        

if __name__ == '__main__':
    timestamp, buses = parse('input')
    assert get_next_departure(939, 59) == 944
    test_timestamp = 939
    test_buses = 7,13,59,31,19
    assert get_earliest_bus(test_timestamp, test_buses) == (944, 59)

    departure, bus = get_earliest_bus(timestamp, buses)

    print(departure, bus, (departure-timestamp) * bus)

    
    test_buses = {i:x for i, x in enumerate((7,13,None,None,59,None,31,19)) if x}
    
    print(find_part_two(test_buses,100000))
    print(find_part_two(parse_two('input'), 100000000000000))