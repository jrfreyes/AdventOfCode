

from typing import Optional


passport_keys = {
    'byr': 'Birth Year',
    'iyr': 'Issue Year',
    'eyr': 'Expiration Year',
    'hgt': 'Height',
    'hcl': 'Hair Color',
    'ecl': 'Eye Color',
    'pid': 'Passport ID',
    'cid': 'Country ID',}

optional_keys = ['cid']
year_keys = ['byr', 'iyr', 'eyr']
hex = '0123456789abcdef'
valid_ecl = 'amb blu brn gry grn hzl oth'.split()

limits = {
    'byr': (1920, 2002),
    'iyr': (2010, 2020),
    'eyr': (2020, 2030),
    'hgt': {
        'cm':(150, 193),
        'in':(59, 76)
    }
}


required_passport_keys = [key for key in passport_keys if key not in optional_keys]

def is_valid_passport(passport: dict, requirement = required_passport_keys ):
    return all((key in passport) for key in requirement)

def is_strictly_valid_passport(passport: dict, requirement = required_passport_keys ):
    if not all((key in passport) for key in requirement):
        return False
    
    if any(not passport[key].isnumeric() for key in year_keys):
        return False
    
    if any(
        not within_limits(
            int(passport[key]),
            *limits[key]
        ) for key in year_keys):
        return False

    hgt = passport['hgt']
    if not hgt[:-2].isnumeric() or hgt[-2:] not in ['cm', 'in']:
        return False
    
    hgt_val, hgt_unit = int(hgt[:-2]), hgt[-2:]
    if not within_limits(hgt_val, *limits['hgt'][hgt_unit]):
        return False
    
    hcl = passport['hcl']
    if hcl[0] != '#' or any(ch.lower() not in hex for ch in hcl[1:]):
        return False

    if passport['ecl'] not in valid_ecl:
        return False

    pid = passport['pid']
    if not pid.isnumeric() or len(pid) != 9:
        return False

    return True 

def within_limits(x, a, b):
    return not(x < a or x > b)

def read_passports(filename):
    with open(filename) as f:
        passports = []
        for line in f.read().split('\n\n'):
            passports.append(dict(tuple(pair.split(':')) for pair in line.strip().split()))
    return passports


if __name__ == '__main__':
    passports = read_passports('input')
    valid_passports = [passport for passport in passports if is_strictly_valid_passport(passport)]
    # print(*valid_passports, sep='\n')
    print(f'Count: {len(valid_passports)}')

    assert within_limits(1,1,1)
    assert within_limits(1,2,1) == False
    assert within_limits(1,0,1)