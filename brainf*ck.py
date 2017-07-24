#-*-coding:utf8;-*-

import os
import sys
import time

#Internal memory size definition
MEMSIZE = 30000

#This class provides internal memory access
class Memory:
    def __init__(self):
        #internal pointer
        self.ptr = 0
        #internal memory
        self.stk = [0] * MEMSIZE
    
    def increase(self):
        self.stk[self.ptr] += 1
    
    def decrease(self):
        self.stk[self.ptr] -= 1
    
    def increase_pointer(self):
        self.ptr += 1
        if self.ptr >= MEMSIZE:
            self.ptr -= MEMSIZE
    
    def decrease_pointer(self):
        self.ptr -= 1
        if self.ptr <= -MEMSIZE:
            self.ptr += MEMSIZE
    
    def get(self):
        self.stk[self.ptr] = ord(sys.stdin.read(1))
    
    def put(self):
        print(chr(self.stk[self.ptr]), end='')
    
    def Is_zero(self):
        return self.stk[self.ptr] == 0

#returns tuple of time from number. the format is (Hour, Minute, Second).
def time_format(tm):
    return (str(round(tm // 3600)), str(round((tm // 60) % 60)), str(round(tm % 60, 5)))

start_time = time.time()
#char pointer in source code.
scp = 0

#The index list in code of found characters "["
lblst = list()

#nest count of square-brankets.
lbnest = 0

try:
    src = open(sys.argv[1])
except:
    print("cannot read file." ,file=sys.stderr)
    sys.exit(1)

#Set debug flag
try:
    dbg = sys.argv[2] == '/d'
except:
    dbg = False

code = src.read()
src.close()

#Create memory instance
stacks = Memory()

#Interpreter main processing part
try:
    while True:
        if len(code) <= scp:
            break
        if dbg:
            print("%s: char %d" % (code[scp], scp))
            print("stack pointer points %d" % stacks.ptr)
        if code[scp] == '>':
            stacks.increase_pointer()
            scp += 1
        elif code[scp] == '<':
            stacks.decrease_pointer()
            scp += 1
        elif code[scp] == '+':
            stacks.increase()
            scp += 1
        elif code[scp] == '-':
            stacks.decrease()
            scp += 1
        elif code[scp] == '.':
            stacks.put()
            scp += 1
        elif code[scp] == ',':
            stacks.get()
            scp += 1
        elif code[scp] == '[':
            if dbg:
                print(lblst)
                print(scp)
                print("Current variable content : %d" % stacks.stk[stacks.ptr])
                print("stacks.Is_zero() = %s" % str(stacks.Is_zero()))
            if not stacks.Is_zero():
                if not scp in lblst:
                    lblst.append(scp)
                    lbnest += 1
                scp += 1
            else:
                nlv = 0
                while True:
                    scp += 1
                    if dbg:
                        print("nest level is %d and additional is %d, basical is %d" % (lbnest + nlv, nlv, lbnest))
                        print("skipping %s: char %d" % (code[scp], scp))
                    if code[scp] == '[':
                        nlv += 1
                        continue
                    if code[scp] == ']' and nlv > 0:
                        nlv -= 1
                        continue
                    if code[scp] == ']':
                        if dbg:
                            print("closing square branket was found. breaking loop.")
                        scp += 1
                        break
        elif code[scp] == ']':
            if dbg:
                print("label list: %s, index: %d" % (str(lblst), lbnest))
            scp = lblst[lbnest - 1]
            del lblst[lbnest - 1]
            lbnest -= 1
        else:
            scp += 1
except:
    #TODO: Make this show details of happened error.
    print("syntax error. executing failed." ,file = sys.stderr)
finally:
    print("\n\nActual execution time: %sh %sm %ss" % time_format(time.time() - start_time))
