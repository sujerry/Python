import sys

try:
    #f1 = open('./B-small-practice.in', 'r');
    f1 = open('./B-large-practice.in', 'r');
    f2 = open('./out.txt', 'w');

    t = int(f1.readline());
    data = []
    sign = 1
    for i in range(1, t+1):
        l = int(f1.readline())
        data = [int(ti) for ti in f1.readline().split()]
        s = int(f1.readline())
        
        f2.write('Case #' + str(sign) + ':')
        sign = sign + 1
        for j in range(s):
            tmp = int(f1.readline())
            num = 0
            for k in range(0, l*2, 2):
                if tmp>=data[k] and tmp<=data[k+1]:
                    num = num + 1
            f2.write(' ' + str(num))
        f2.write('\n')
        f1.readline()

finally:
    if f1:
        f1.close()
    if f2:
        f2.close()

