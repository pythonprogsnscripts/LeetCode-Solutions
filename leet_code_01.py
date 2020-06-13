def split_string(string):

    '''
    Split string 
    '''

    dict_left = {}
    dict_right = {}

    uniq_left = 0
    uniq_right = 0

    counter = 0

    for i in range(len(string)):
        uniq_right = add_to_dict(string[i], dict_right, uniq_right)

    for i in range(len(string)):

        if uniq_left == uniq_right:
            counter+=1

        uniq_left = add_to_dict(string[i], dict_left, uniq_left)
        uniq_right = remove_from_dict(string[i], dict_right, uniq_right)

    return counter


def add_to_dict(char, _dict, uniq):

    print('-->',char)
    print('dict',_dict)
    print('uniq', uniq)

    if not char in _dict:
        _dict[char] = 1
        uniq+=1
    else:
        _dict[char]+=1
    return uniq

def remove_from_dict(char, _dict, uniq):

    print('-----------------------------------')
    print('R -->',char)
    print('R --> dict',_dict)
    print('R --> uniq', uniq)
    print('-----------------------------------')

    if char in _dict:
        _dict[char]-=1

    if _dict[char] == 0:
        uniq-=1
    return uniq

if __name__ == "__main__":
    s1 = "ababa"

    print(split_string(s1))
