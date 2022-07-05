def check(string):
    valid_open = ['<', '{', '[']
    valid_close = ['>', '}', ']']
    open = []

    if(len(string) > 4096):
        return False

    for x in string:
        if(x in valid_open):
            open.insert(0, x)

        elif(x in valid_close):
            if(len(open) > 0 and open[0] == valid_open[valid_close.index(x)]):
                open.pop(0)
            else:
                return False
        else:
            return False

    if(len(open) > 0):
        return False
    else:
        return True

# main process
string = input('Input string: ')
print(check(string))
