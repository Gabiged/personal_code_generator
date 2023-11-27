
def person_code(date_, birth_line):
    """function to generate personal code 2nd to 8th digit"""
    birth_split = date_.split("-")
    year = birth_split[0][2:]
    month = birth_split[1]
    day = birth_split[2]
    l_code = year + month + day + birth_line[0] + birth_line[1] + birth_line[2]
    return l_code


def first_code_no(sex_person):
    """function to generate 1st digit(female or male)"""
    l_code2 = person_code(date_of_birth, birth_sequence)
    if sex_person == "Female":
        if l_code2[0] != 2:
            first = 4
        elif l_code2[0] == 2:
            first = 6
    else:
        if l_code2[0] != 2:
            first = 3
        else:
            first = 5
    return first


def control_no():
    '''function to generate last control digit. Formula is official from Wiki'''
    partial_code = person_code(date_of_birth, birth_sequence)
    a = first_code_no(sex)
    b = int(partial_code[0])
    c = int(partial_code[1])
    d = int(partial_code[2])
    e = int(partial_code[3])
    f = int(partial_code[4])
    g = int(partial_code[5])
    h = int(partial_code[6])
    i = int(partial_code[7])
    j = int(partial_code[8])
    s = (a * 1) + (b * 2) + (c * 3) + (d * 4) + (e * 5) + (f * 6) + (g * 7) + (h * 8) + (i * 9) + (j * 1)
    if s % 11 != 10:
        k = s % 11
        return k
    else:
        s = a * 3 + b * 4 + c * 5 + d * 6 + e * 7 + f * 8 + g * 9 + h * 1 + i * 2 + j * 3
        if s % 11 != 10:
            k = s % 11
            return k
        else:
            k = 0
            return k


def personal_code_validator(p_code):
    '''function to validate given personal code(not generated)'''
    last_digit = int(str(p_code)[-1])
    if last_digit == control_no():
        print('Valid')
    else:
        print('Not valid')


sex = 'Female'
date_of_birth = '1979-02-19'
birth_sequence = '070'
outcome = f'{first_code_no(sex)}{person_code(date_of_birth, birth_sequence)}{control_no()}'
print(outcome)
personal_code_validator(383052017840)
