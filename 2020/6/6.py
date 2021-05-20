

def get_count(s):
    return len(set(''.join(s.strip().split())))

def get_count_two(s):
    lines = s.strip().split()
    q_sets = [set(line) for line in lines]
    return len(set(''.join(lines)).intersection(*q_sets))

if __name__ == '__main__':
    with open('input') as f:
        counts = []
        counts_two = []
        for grp in f.read().strip().split('\n\n'):
            counts.append(get_count(grp))
            counts_two.append(get_count_two(grp))
        print(sum(counts))
        print(sum(counts_two))
        
