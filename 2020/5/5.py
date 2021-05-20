
def get_row(boarding_pass) -> int:
    row_start = 0
    row_end = 127
    size = 128
    for ch in boarding_pass[:-3]:
        size //= 2
        if ch == 'F':
            row_end -= size
        elif ch == 'B':
            row_start += size
    assert row_start == row_end
    return row_start

def get_column(boarding_pass) -> int:
    start = 0
    end = 7
    size = 8
    for ch in boarding_pass[-3:]:
        size //= 2
        if ch == 'L':
            end -= size
        elif ch == 'R':
            start += size
    assert start == end
    return start

def get_seatid(boarding_pass) -> int:
    return get_row(boarding_pass) * 8 + get_column(boarding_pass)

def get_missing_seat(seatids) -> int:
    seatids = sorted(seatids)
    for x, y in zip(seatids[:-1], seatids[1:]):
        if y == x + 2:
            return (x + y) // 2

if __name__ == '__main__':
    with open('input') as f:
        seatids = []
        for line in f:
            seatids.append(get_seatid(line.strip()))
        print(max(seatids))
        print(get_missing_seat(seatids))