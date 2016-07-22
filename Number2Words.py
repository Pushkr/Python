# program to convert numbers below(but not including) 10 million to words

import random

def getword(num):
    dict_dollars = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
                    5: "five", 6: "six", 7: "seven", 8: "eight",
                    9: "nine", 11: "eleven", 10: "ten", 12: "twelve",
                    13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
                    17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty",
                    30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy",
                    80: "eighty", 90: "ninety"}
    return str(dict_dollars.get(num))


def getunder100(num):
    if num <= 20 or num % 10 == 0:
        return getword(num)
    else:
        return getword(num // 10 * 10) + " " + getword(num % 10)


def convertor(amount):
    smount = str(amount)

    if len(smount) > 7:
        print("Amount over 9 million is not supported")
        return

    while len(smount) != 7:
        smount = " " + smount

    desc = ""

    if len(smount[0].strip()) > 0:
        desc += getword(int(smount[0])) + " million, "
    if len(smount[1].strip()) > 0:
        desc = desc + getword(int(smount[1])) + " hundred, "
    if len(smount[2:4].strip()) == 2:
        desc += getunder100(int(smount[2] + smount[3])) + " thousand, "
    elif len(smount[2:4].strip()) > 0:
        desc += getword(int(smount[2:4].strip())) + " thousand, "
    if len(smount[4].strip()) > 0:
        desc += getword(int(smount[4])) + " hundred "
    if len(smount[5:].strip()) == 2 and (int(smount[5:]) > 0):
                desc +=  getunder100(int(smount[5] + smount[6]))
    elif len(smount[5:].strip()) > 0 and (int(smount[5:]) > 0):
        desc += getword(int(smount[5:].strip()))

    # desc += " dollars "
    return (desc.capitalize())

# sample usage:
num = random.choice(range(0,1000000))
print("%d : %s"%(num,convertor(num)))

#sample usage:
for i in range(99,0,-1):
    print(convertor(i), "Bottles of beer on the wall,")
    print(convertor(i), "bottles of beer.")
    print("Take one down and pass it around,")
    if i == 1:
        print("No more bottles of beer on the wall.")
    else:
        print(convertor(i-1), "bottles of beer on the wall.")
