"""Python program for factorial of a number """
num=int(input("Enter any Number"))
fact=1
if num<0:
    print("Factorial not exist for negative numbers")
else:
    for i in range(1,num+1):
        fact=fact*i
    print(f"factorial of the {num} is {fact}")
