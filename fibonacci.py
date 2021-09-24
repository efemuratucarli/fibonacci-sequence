"""
Created on Fri Sep 24 20:13:58 2021

@author: efemuratucarli
""" 

#The aim of this script is comparing two different methods for calculating fibonacci terms.

number_of_recursive_calls  = 0

def fib(x):
    # In order to make the number_of_recursive_calls variable accessible outside scope of the function,
    # I need to make it global
    global number_of_recursive_calls 
    number_of_recursive_calls += 1
    if x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        return fib(x-1) + fib(x-2)
    
print(fib(25))
print("the number of fibonacci call",number_of_recursive_calls)
print("----------")

number_of_recursive_calls2 = 0
base_values = {1:0,2:1}

def fib_efficient(x,y):
    # In order to make the number_of_recursive_calls variable accessible outside scope of the function
    # I need to make it global
    global number_of_recursive_calls2
    number_of_recursive_calls2 += 1
    if x in y:
        return y[x]
    else:
       ans = fib_efficient(x-1,y) + fib_efficient(x-2,y)
       # I am storing the values that I have calculated, in order to not compute the terms that I have computed before
       base_values[x] = ans
       return ans

print(fib_efficient(25,base_values))
print("the number of fibonacci call",number_of_recursive_calls2)

# we can see that when we store the values that we calculated before,the computing process become faster