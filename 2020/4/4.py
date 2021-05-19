

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
    
    byr, iyr, eyr = (int(passport[key]) for key in year_keys)
    if any((
        byr < 1920, byr > 2002,
        iyr < 2010, iyr > 2020,
        eyr < 2020, eyr > 2030
        )):
        return False

    hgt = passport['hgt']
    if not hgt[:-2].isnumeric() or hgt[-2:] not in ['cm', 'in']:
        return False
    
    hgt_val, hgt_unit = int(hgt[:-2]), hgt[-2:]
    
    return True 

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