"""practice with funtions"""

from random import randint

# print(randint(3, 17))


"""Class Work"""


# Funtion definition
def sum(num1: int, num2: int) -> int:
    """return the sum of num1 and num2"""
    return num1 + num2


num1 = randint(1, 100)
num2 = randint(1, 100)

# Functin call
print(sum(num1, num2))

#### wants us to do it like print(sum(num1=1, num2=43)) #####
