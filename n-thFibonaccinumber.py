""" Python Program for n-th Fibonacci number"""
n=int(input("Enter the number you want to find"))
first,current=0,1
for i in range(0,n):
    if i<=1:
        next=i
    else:
        next=first+current
        first=current
        current=next
print(f" the {n}th fibonacci number is={next} ")