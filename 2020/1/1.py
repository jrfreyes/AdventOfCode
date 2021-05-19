
def find_two_numbers_with_sum(nums, sum):
    for x in nums:
        for y in nums:
            if x + y == sum:
                return x, y

def find_three_numbers_with_sum(nums, sum_):
    for x in nums:
        for y in nums:
            for z in nums:
                if sum((x, y, z)) == sum_:
                    return x, y, z


def find_n_numbers_with_sum(nums, sum, n):
    ret_val = []
    for x in nums:
        if n == 1 and x == sum:
            return [x]
        elif n > 1:
            ret_val.extend(find_n_numbers_with_sum(nums, sum - x, n - 1))
    return set(ret_val)
        

def product(*factors):
    x = 1
    for y in factors:
        x *= y
    return x

if __name__ == '__main__':
    with open('1.txt') as f:
        nums = [int(line) for line in f if not line.isspace()]
        x, y = find_two_numbers_with_sum(nums, 2020)
        print(x * y)
        n = find_n_numbers_with_sum(nums, 2020, 3)
        p = product(*n)
        print(n, p)
        n = find_three_numbers_with_sum(nums, 2020)
        p = product(*n)
        print(n, p)
        # print(*(line for line in f if not line.isspace()))    