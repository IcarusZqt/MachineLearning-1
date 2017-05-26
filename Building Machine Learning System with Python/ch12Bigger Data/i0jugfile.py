from jug import TaskGenerator
from time import sleep

@TaskGenerator
def double(x):
    sleep(4)
    return 2 * x


@TaskGenerator
def add(a, b):
    return a + b


@TaskGenerator
def print_final_result(oname, value):
    with open(oname, 'w') as output:
        output.write("Final result: {0}\n".format(value))


input = 2
y = double(input)
z = double(y)

y2 = double(7)
z2 = double(y2)
print_final_result('output.txt', add(z, z2))

# 执行： jug execute i0jugfile.py 