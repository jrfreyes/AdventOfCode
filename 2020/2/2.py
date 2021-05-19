
def is_valid(lower_limit: int, upper_limit: int, letter: str, password: str):
    n_letter = password.count(letter)
    return n_letter >= lower_limit and n_letter <= upper_limit

def is_valid2(a, b, letter, password: str):
    try:
        return [password[a - 1], password[b - 1]].count(letter) == 1
    except Exception as e:
        print(a, b, letter, password, len(password),  e)
        raise e


def part_one():
    valid_passwords = []
    with open('input') as f:
        for line in f:
            limits, letter, password = line.strip().split(' ')
            a, b = map(int, limits.split('-'))
            letter = letter.strip().strip(':')
            if is_valid(a, b, letter, password):
                valid_passwords.append(((a,b), letter, password))
    print(valid_passwords)
    print(len(valid_passwords))

if __name__ == '__main__':
    valid_passwords = []
    valid_passwords2 = []
    with open('input') as f:
        for line in f:
            limits, letter, password = line.strip().split(' ')
            a, b = map(int, limits.split('-'))
            letter = letter.strip().strip(':')
            if is_valid(a, b, letter, password):
                valid_passwords.append(((a,b), letter, password))
            if is_valid2(a, b, letter, password):
                valid_passwords2.append(((a,b), letter, password))
    print(valid_passwords)
    print(len(valid_passwords))
    print('---------')
    print(valid_passwords2)
    print(len(valid_passwords2))
    