
def check(data):
    result = []
    last_check = len(data)
    find_first = 0
    find_second = 0
    i = 1
    while i <= len(data):
        j = i + 1
        while j <= last_check:
            if (data[i] == data[j]):
                # for new set string
                if(find_first != 0):
                    result.clear()

                last_check = j
                find_first = i
                find_second = j
                result.append(i)
                result.append(j)
                break
            j += 1
        i += 1

    # if find set string, continue search until last index
    if(find_second):
        i = find_second + 1
        while(i <= len(data)):
            if(data[i] == data[find_first]):
                result.append(i)
            i += 1

    return result

# main process
data = {}
count = int(input("Jumlah input: "))
i = 1
while i <= count:
    data[i] = input(f"Input kata #{i}: ")
    i += 1

result = check(data)
if(len(result) > 0):
    print(result)
else:
    print("false")
