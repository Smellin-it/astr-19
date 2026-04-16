# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 17:33:37 2026

@author: upnup
"""

def Awesomeresult():
    print("YAY!")
def Awesomeequation(x=0.0):
    a=x**3+8
    if a>27:
        Awesomeresult()
    return(a)
def main():
    print(Awesomeequation(9))

if __name__ == "__main__":
    main()
