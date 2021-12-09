

def PartOne(nums):
    num_increased = 0

    for prev, x in zip(nums[:-1], nums[1:]):
        if x > prev:
            num_increased += 1

    return num_increased

def PartTwo(nums):
    sums = [sum(nums[i:i+3]) for i in range(len(nums) - 2)]
    return PartOne(sums)

if __name__ == '__main__':
    with open('input') as f:
        nums = [int(x) for x in f]
    print(f'{PartOne(nums) = }')
    print(f'{PartTwo(nums) = }')
