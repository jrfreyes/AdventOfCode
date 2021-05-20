from functools import cache

def use_all(adapters):
    adapters = sorted(adapters)
    adapters.append(adapters[-1] + 3)
    
    jolt_diffs = {}
    curr_jolt_rating = 0

    for adapter in adapters:
        diff = adapter - curr_jolt_rating
        if diff not in jolt_diffs:
            jolt_diffs[diff] = 1
        else:
            jolt_diffs[diff] += 1
        curr_jolt_rating = adapter

    return jolt_diffs

class CombinationTree:
    def __init__(self, adapters):
        self.children = {}
        adapters = sorted(adapters)
        for jolt in [0] + adapters:
            self.children[jolt] = []
            for j in range(jolt + 1, jolt + 4):
                if j in adapters:
                    self.children[jolt].append(j)

    @cache # learned about functools thanks to 0xdf https://0xdf.gitlab.io/adventofcode2020/10
    def count_combinations(self, jolt = 0):
        if len(self.children[jolt]) == 0:
            return 1
        return sum(self.count_combinations(child) for child in self.children[jolt]) 

                
def product(*factors):
    p = 1
    for x in factors:
        p *= x
    return p

if __name__ == '__main__':
    with open('input') as f:
        adapters = [int(x.strip()) for x in f if x.strip().isnumeric()]
        print(adapters)
        diffs = use_all(adapters)
        print(diffs)
        print(diffs[1] * diffs[3])
        com_tree = CombinationTree(adapters)
        print(com_tree.children)
        print(com_tree.count_combinations())