def prime_checker(number):
    if n <=1:
        print("Not Prime")
        return
    
    for i in range(2, number):
        if n % i == 0:
            print("Not Prime")
            return
        
    print("Prime")

n = int(input("Ask a number: "))
prime_checker(n)