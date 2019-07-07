import math
import sys
from os import rename


print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    test = "test"
    greeting = "hello,{}".format(who_to_greet)
    return greeting


print(greet("world"))
print(greet("Corey"))
