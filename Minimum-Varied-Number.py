tt = int(input())

while tt:
    number = int(input())
    total = 0
    digits = []
    for i in range(9,0,-1):
        if (total + i) < number:
            # print(digits)
            digits.append(i)
            total += i
        else:
            digits.append((number - total))
            print(int(''.join(map(str, digits[::-1]))))
            digits = []
            break

    tt -= 1