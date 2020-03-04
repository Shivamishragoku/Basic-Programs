"""
Python Program for Fibonacci numbers

The Fibonacci numbers are the numbers in the following integer sequence.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …….."""
n=int(input("Enter the the number of terms"))
first=0
current=1
for i in range(0,n):
    if i<=1:
        next=0
    else:
        next=first+current
        first=current
        current=next
    print(next,end=",")


