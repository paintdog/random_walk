import matplotlib.pyplot as plt
from random import choice, randint


upper_limit = 12
value = 10           # initial value


change = [(i / 10) for i in range(1, upper_limit)]
values = []


for i in range(220):
    if randint(0,1):
        value += choice(change)
    else:
        value -= choice(change)
        if value < 0:
            value *= -1
    values.append(value)

        
plt.plot(values)
# plt.ylabel('y axis')
plt.show()
