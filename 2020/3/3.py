
def traverse(terrain, right, down):
    x = right
    y = down
    width = len(terrain[0])
    height = len(terrain)
    
    while y < height:
        yield terrain[y][x]
        x += right
        x %= width
        y += down

def count_trees(terrain, right, down, ch = '#'):
    return len([s for s in traverse(terrain, right, down) if s == ch])

def product(*factors):
    x = 1
    for y in factors:
        x *= y
    return x


if __name__ == '__main__':
    with open('input') as f:
        terrain = [line.strip() for line in f if not line.isspace()]
        right = 3
        down = 1
        ch = '#'

        print(count_trees(terrain, right, down, ch))

        rights = [1, 3, 5, 7, 1]
        downs = [1, 1, 1, 1, 2]

        counts = [count_trees(terrain, r, d, ch) for r, d in zip(rights, downs)]
        print(counts)
        print(product(*counts))

