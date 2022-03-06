
import sys
import time


def ceaser(text):
    type_effect("there is problem here with repeated letters support coming soon", 0.09)
    shift_key = 8
    table = {
        55: ' ', 1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L',
        13: 'M',
        14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y',
        27: 'Z', 28: 'a', 29: 'b', 30: 'c', 31: 'd', 32: 'e', 33: 'f', 34: 'g', 35: 'h', 36: 'i', 37: 'j', 38: 'k',
        39: 'l', 40: 'm', 41: 'n', 42: 'o', 43: 'p', 44: 'q', 45: 'r', 46: 's', 47: 't', 48: 'u', 49: 'v', 50: 'w',
        51: 'x', 52: 'y', 53: 'z'
    }
    temp = dict()
    for i in text:
        for k in table:
            if table[k] == i:
                new = k + shift_key
                if new > 56:
                    new = new % 55
                    temp[new] = table[new]
                    print(temp)
                    print(new)
                else:
                    print(new)
                    temp[new] = table[new]
                    print(temp)
    ls = temp.values()
    print(ls)
    st1 = ' '
    for i in ls:
        st1 += i
    print(st1)
    return st1


def type_effect(string, delay):
    for char in string:
        time.sleep(delay)
        sys.stderr.write(char)










