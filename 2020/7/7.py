

class Bag:
    bags = {}
    def __init__(self, rule: str) -> None:
        color, contents = rule.strip().split(' contain ')
        self.color = ' '.join(color.split()[:-1])

        contents = [bag.strip('.').split() for bag in contents.split(', ') if bag != 'no other bags.']
        self.contents = {' '.join(bag[1:-1]): int(bag[0]) for bag in contents}

        Bag.bags[self.color] = self

    def contains_bag(self, color) -> bool:
        if color in self.contents:
            return True
        for bag in self.contents:
            if Bag.bags[bag].contains_bag(color):
                return True

    def bag_count(self) -> int:
        count = 1
        if len(self.contents) == 0:
            return count
        for color in self.contents:
            count += self.contents[color] * Bag.bags[color].bag_count() 
        return count

    def __str__(self) -> str:
        contents = []
        for color in self.contents:
            s = 's' if self.contents[color] > 1 else ''
            contents.append(f'{self.contents[color]} {color} bag{s}')
        contents = ', '.join(contents)
        return f'{self.color} bags contain {contents}.'

    def __repr__(self) -> str:
        return str(self.contents)

if __name__ == '__main__':
    with open('input') as f:
        for line in f:
            Bag(line)

    count = 0
    for color in Bag.bags:
        if Bag.bags[color].contains_bag('shiny gold'):
            count += 1
    print(count)
    print(Bag.bags['shiny gold'].bag_count() - 1)