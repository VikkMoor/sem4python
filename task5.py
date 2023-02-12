"""Form the sum of polynomials from two files"""

from random import Random, randint
my_list = []
f1 = open('polynomial_1.txt', 'w')
f2 = open('polynomial_2.txt', 'w')
f3 = open('sum_polynomial.txt', 'w')
for i in range(8):
    num = randint(0, 100)
    my_list.append(num)

polynomial1 = f"{my_list[0]}*x^{my_list[1]} + {my_list[2]}*x^{my_list[3]}"
f1.write(str(polynomial1))
f1.close()
polynomial2 = f"{my_list[4]}*x^{my_list[5]} + {my_list[6]}*x^{my_list[7]}"
f2.write(str(polynomial2))
f2.close()

file1 = 'polynomial_1.txt'
file2 = 'polynomial_2.txt'
fil1 = open(file1, 'r')
fil2 = open(file2, 'r')

for line1 in fil1:
    line1
for line2 in fil2:
    line2

sum_polynomial = f"({line1}) + ({line2})"
f3.write(str(sum_polynomial))

print(f"({line1}) + ({line2})")
fil1.close()
fil2.close()
f3.close()