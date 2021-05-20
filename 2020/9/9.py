

def check_valid(value, preamble, n = 2, **kwargs):
    # if ''
    assert len(preamble) == 25, f'Length: {len(preamble), preamble}'
    preamble = sorted(preamble, reverse = True)
    if value > sum(preamble[:n]):
        return False
    
    preamble = [x for x in preamble if x <= value]
    if len(preamble) < n:
        return False

    for x in preamble:
        for y in preamble:
            if x == y:
                continue
            if x + y == value:
                return True
    return False

def find_weakness(nums, invalid_num):
    a = 0
    b = 1

    while a < len(nums) and b < len(nums):
        curr_list = nums[a:b]
        curr_sum = sum(curr_list)
        if curr_sum < invalid_num:
            b += 1
        elif curr_sum > invalid_num:
            a += 1
        else:
            return min(curr_list) + max(curr_list)

if __name__ == '__main__':
    with open('input') as f:
        nums = [int(x) for x in f]
        preamble = nums[:25]
        valid_nums = [x for i, x in enumerate(nums[25:], 25) if check_valid(x, nums[i - 25:i])]
        invalid_nums = [x for i, x in enumerate(nums[25:], 25) if not check_valid(x, nums[i - 25:i])]
        print(valid_nums, len(valid_nums))
        print(invalid_nums)
        print(find_weakness(nums, invalid_nums[0]))