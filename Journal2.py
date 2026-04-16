# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 17:46:20 2026

@author: Administrator
"""

def floating_sum(a,b):
    Sum = a+b
    return Sum

def integer_diff(c,d):
    Diff= c-d
    return Diff

def main():
   print("1.111111111 plus 3.14159265 is equal to", floating_sum(1.11111111, 3.14159265))
   print("The difference between 10 and 3 is equal to", integer_diff(10, 3))
   print("The product of these two numbers is equal to", floating_sum(1.11111111, 3.14159265)*integer_diff(10, 3))
if __name__ == "__main__":
    main()
