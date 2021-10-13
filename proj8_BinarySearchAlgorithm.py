#learnt from Youtuber - Telusko

position = 0

def binary(set, number):
    low_limit = 0
    upper_limit = len(set) - 1

    while low_limit <= upper_limit:
        n = (low_limit + upper_limit)//2
        if number == set[n]:
            globals()['position'] = n
            return True
        else:
            if number < set[n]:
                upper_limit = n
            else:
            #elif number > set[n]:
                low_limit = n

    return False

set = []
for i in range(0, 100, 2):
    set.append(i)

list(map(int, set))
print(set)

number = int(input("Enter A Number: "))

if binary(set, number):
    #if true
    print("Number is at position", position + 1)
