# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 17:47:14 2026

@author: upnup
"""

class Animal:  
    def __init__(self, arms=0.0, legs=0.0, eyes=0, tail=False, furry=False): 
        self.arms=arms
        self.legs=legs
        self.eyes=eyes
        self.tail=tail
        self.furry=furry
    
    def printAnimal(self):
        print("Your animal's characteristics are:")
      
        if self.arms==0.0:
            print("No arms,")
        else:
            print(self.arms, "meter long arms,")
       
        if self.legs==0.0:
            print("Has no legs,")
        else:
            print(self.legs, "meter long legs,")
       
        if self.eyes==0:
            print("Has no eyes,")
        else:
            print("has", self.eyes, "eyes,")
        
        if self.tail==False:
            print("Doesn't have a tail")
        else: 
            print("Has a tail")
       
        if self.furry==False:
            print("And is furless")
        else:
            print("And is furry")

def main():
    Elliots_Animal= Animal(arms= 0.0, legs= 0.1, eyes= 2, tail=False, furry=True)
    print(Elliots_Animal.printAnimal())

if __name__ == "__main__":
    main()

            