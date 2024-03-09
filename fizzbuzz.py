

for i in range(1, 101):

    #if the number is a multiple of 3 and 5, print "FizzBuzz"
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    
    #if the number is a multiple of 3, print "Fizz"
    elif i % 3 == 0:
        print("Fizz")
    
    #if the number is a multiple of 5, print "Buzz"
    elif i % 5 == 0:
        print("Buzz")
    
    #Print all other numbers
    else:
        print(i)