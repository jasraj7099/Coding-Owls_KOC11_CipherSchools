# Defining a function to check for prime number and composite number in a range

def PrimeOrComposite(n1, n2):

    prime = 0                                   # variable to count the number of prime numbers in the given range
    composite = 0                               # variable to count the number of composite numbers in the given range

    for i in range(n1, n2+1):

        factor = 0                              # variable to count the number of factors of every number

        for j in range(1, i+1) :
            if i % j == 0 :
                factor = factor + 1
        if factor == 2 :                        # checking the number of factor of every number                  
            prime = prime + 1
            print(i,"is prime")
        elif factor == 1:
            print(i,"is neither prime nor composite")
        else :
            composite = composite + 1
            print(i,"is composite")
    print(prime,"prime and",composite,"composite numbers in the range")

# Taking the input from the user 

A = int(input("Enter the lower limit, A: "))
B = int(input("Enter the upper limit, B: "))

# Calling the function and assigning the range to it

PrimeOrComposite(A, B)