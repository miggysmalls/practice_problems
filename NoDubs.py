STRING = 'abcdddddeefghhhiijkkkkklmmnooprssstuvwxyzzzz'


def no_dubs(x):
    #   Empty list that will have chars without duplicates.
    no_dubs_string = []
    #   Add char to no_dubs_string if it hasn't already been added.
    [no_dubs_string.append(i) for i in x if i not in no_dubs_string]
    return no_dubs_string

if __name__ == '__main__':
    a = no_dubs(STRING)
    print(''.join(a))