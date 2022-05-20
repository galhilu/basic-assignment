def invalidinp():
    print("error")
    exit()
def q1():
    str = input()
    goodchar=0
    for i in range(0,len(str)):
        if ord(str[i])>96 and ord(str[i])<123:   # if lowercase letter
            if str[i]!='a' and str[i]!='e' and str[i]!='i' and str[i]!='o' and str[i]!='u' and str[i]!='y':
                goodchar=goodchar+1
        elif ord(str[i])>64 and ord(str[i])<91:   # if uppercase letter
            goodchar = goodchar + 1
    print(goodchar)
    exit()
def q2():
    try:
        x = float(input())
        n = int(input())
    except:
        invalidinp()
    if n < 0:
        print("error")  # invalid input
        exit()
    prvpart = 0
    curentpart = 0
    for i in range(1, n + 1):
        curentpart = (x ** i) / i * (-1) ** (i - 1)
        prvpart = prvpart + curentpart

    print(prvpart)
    exit()
def q3():
        inputstr = input()
        splitstr = inputstr.split()
        even = []
        odd = []
        for i in range(0, len(splitstr)):                # the odd and even are switched
            if (i + 1) % 2 == 0:                         # because I started to count indexes
                odd.append(splitstr[i])                  # and string indexes start from 0
            else:
                even.append(splitstr[i])

        even.sort()
        evenstr = ""
        for i in range(0, len(even)):
            evenstr = evenstr + " " + even[i]

        odd.sort(reverse=True)
        oddstr = ""
        for i in range(0, len(odd)):
            oddstr = oddstr + " " + odd[i]

        print(evenstr.upper() + oddstr.lower())
        exit()
def q4():
    try:
        inpnum = int(input())
    except:
        invalidinp()

    def invers(num):
        inversnum = 0
        while (num > 0):
            remainder = num % 10
            inversnum = (inversnum * 10) + remainder
            num = num // 10
        return inversnum

    for i in range(0, 500):
        if str(inpnum) == str(inpnum)[::-1]:  # plindrom check
            print(i)
            exit()
        invernum = invers(inpnum)
        inpnum = invernum + inpnum
    print("true")  # will reach only if passed 500 iterations
    exit()
try:
    qnum=int(input())
except:
    invalidinp()

if qnum==1:
    q1()
if qnum==2:
    q2()
if qnum==3:
    q3()
if qnum==4:
    q4()
invalidinp()