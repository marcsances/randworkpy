#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse,random,sys

data=[0,0]

def run():
    op=random.randint(0,10)
    if (op in (1,2)):
        sys.stdout.write(chr(data[random.randint(0,1)]))
    elif (op==3):
        sys.stdout.write('\a')
    elif (op in (4,5)):
        data[op-4]=random.randint(0,255)
    elif (op in (6,7)):
        data[op-6]=0
    elif (op==8):
        data[0]=(data[0]+data[1])%256
    elif (op in (9,10)):
        sys.stdout.write(chr(data[op-9]))

def main(args):
    with open(args.filename) as f:
        ir = len([x for x in f.readlines() if x.strip()=="Do anything"])
        while (ir>0):
            run()
            ir=ir-1

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Randwork interpreter')
    parser.add_argument('filename')
    args = parser.parse_args()
    random.seed()
    main(args)