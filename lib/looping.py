#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    num = 10
    while num > 1:
        print(num)
        num = num - 1
    print("Happy New Year!")
        
        
pass

def square_integers(int_list):
    # code goes here!
    return[num ** 2 for num in int_list]
    pass

def fizzbuzz():
    # code goes here!
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
    pass

fizzbuzz()

        
    

