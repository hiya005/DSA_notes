def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
nterms= int(input("enter number of terms:"))

if nterms <= 0:
    print("enter valid terms")
else:
    print("fibonnaci sequence:")
    for i in range(nterms):
        print(fibonacci(i))