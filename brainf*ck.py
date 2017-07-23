#-*-coding:utf8;-*-
#qpy:3
#qpy:console

import os
import sys

class Ptr:
    def __init__(self):
        self.ptr = 0
        self.stk = [0] * 3000
    def increase(self):
        self.stk[self.ptr] += 1
    def decrease(self):
        self.stk[self.ptr] -= 1
    def increase_pointer(self):
        self.ptr += 1
        if self.ptr >= 3000:
            self.ptr -= 3000
    def decrease_pointer(self):
        self.ptr -= 1
        if self.ptr <= 3000
            self.ptr += 3000
    def get(self):
        self.stk[self.ptr] = ord(sys.stdin.read(1))
    def put(self):
        print(chr(self.stk[self.ptr]), end='')
    def Is_zero(self):
        return self.stk[self.ptr] == 0

scp = 0
lblst = list()
lbnest = 0
try:
    src = open(sys.argv[1])
except:
    print("cannot read file." ,file=sys.stderr)
    sys.exit(1)
code = src.read()
src.close()

stacks = Ptr()

while True:
    if len(code) == scp:
        break
    if code[scp] == '>':
        stacks.increase_pointer()
    elif code[scp] == '<':
        stacks.decrease_pointer()
    elif code[scp] == '+':
        stacks.increase()
    elif code[scp] == '-':
        stacks.decrease()
    elif code[scp] == '.':
        stacks.put()
    elif code[scp] == ',':
        stacks.get()
    elif code[scp] == '[':
        if not scp in lblst:
            lblst.append(scp)
            lbnest += 1
        if not stacks.Is_zero():
            pass
        else:
            while True:
                scp += 1
                if code[scp] == ']':
                    scp += 1
                    break
    elif code[scp] == ']':
        scp = lblst[lbnest - 1]
        lbnest -= 1
    else:
        scp += 1
