#!/usr/bin/env python

import random

print("\n***********[Strong Random Password Generator]***********\n")

try:

    A = int(input('\033[1;32mEnter your Password Length (10 to 74) = \033[1;m'))
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    passlen = (A)
    p = "".join(random.sample(s, passlen))

except (SyntaxError, ValueError): ## Python3X

    print("Empty Input or Wrong Input Value")

else:

    print('\n\033[1;35mYOUR SECURE PASSWORD = %s \033[1;m\n' %p)
