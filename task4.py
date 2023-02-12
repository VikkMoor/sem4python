"""Transform the polynomial into the same one but in power k"""

from random import Random, randint

number = int(input("Enter natural value of power k: "))
st = ""
start = number
f = open('dz4.txt', 'w')

while start >= 0:
    num = randint(0, 100)
    if start > 1:
        st += f'{num}x^{start}'
    elif start == 1:
        st += f'{num}x'
    elif start == 0:
        st += f'{num} = 0'
    if start > 0:
        st += ' + '
    start -= 1

f.write(str(st))
f.close()

print(st)
